import os
import requests
from dotenv import load_dotenv
import redis
import logging

# env
load_dotenv()
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")

# redis
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASSWORD)

KAKAO_SEARCH_REQUEST_URL = "https://dapi.kakao.com/v2/local/search/keyword.json?query="


# 카카오 맵 API로 가게 검색
def count_store_by_location_with_kakao(gu, dong_list, store_name):
    store_count = 0

    for dong in dong_list:
        name = f"{gu}:{dong}"
        key = store_name

        if not redis_client.hexists(name, key):
            lock_key = f"{name}:{key}"
            logging.info(f"lock_key = {lock_key}")
            if redis_client.setnx(lock_key, 1):
                try:
                    count, api_status = count_store_by_new_location(gu, dong, store_name)
                    if api_status:
                        redis_client.hset(name, key, count)
                        store_count += count
                        logging.info(f"[검색 API] {name}:{key} = {count}")
                finally:
                    redis_client.expire(lock_key, 1)
        else:
            value = int(redis_client.hget(name, key))
            logging.info(f"[redis] {name}:{key} = {value}")
            store_count += int(redis_client.hget(name, key))

    return store_count, True


def count_store_by_new_location(gu, dong, store_name):
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    count = 0
    api_status = True

    query = f"{gu} {dong} {store_name}"
    url = f"{KAKAO_SEARCH_REQUEST_URL}{query}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        places = response.json().get('documents', [])
        count += len(places)
    except requests.exceptions.HTTPError as http_err:
        print(f"[Kakao Search API] HTTPError {http_err}")
        api_status = False
    except requests.exceptions.RequestException as err:
        print(f"[Kakao Search API] RequestException {err}")
        api_status = False

    return count, api_status


# 서울시 상권 API 비동기 호출 함수
async def fetch_sangwon_data(session, api_key, start_index, end_index):
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/xml/VwsmSignguStorW/{start_index}/{end_index}/"
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"[서울시 상권 조회] Error: {response.status}")
            return None