from dotenv import load_dotenv
import os
from datetime import datetime
from brand_startup_cost import get_brand_fntn_stats
from brand_info import calc_total_brand_count, save_brand_info
import pymysql
import time # time 라이브러리 import

def main():
    load_dotenv()
    # DB 정보
    connection = pymysql.connect(
        host=os.environ.get('HOST'),
        user=os.environ.get('USER'),
        password=os.environ.get('PASSWORD'), 
        charset='utf8'
    )
    cursor = connection.cursor()

    brand_fntn_info = {}  # 창업 비용 정보
    for year in range(datetime.now().year - 1, 2017, -1):
        get_brand_fntn_stats(brand_fntn_info, year)

    print("브랜드 창업 비용 정보 총 개수:", len(brand_fntn_info))

    year = 2023
    total_brand_count = calc_total_brand_count(year)

    data_count = 1000
    page_count = total_brand_count / data_count
    if total_brand_count % data_count != 0:
        page_count += 1

    print(year, "브랜드 총 개수:", total_brand_count)

    start = time.time() # 시작
    for page in range(1, 2):
        save_brand_info(page, data_count, brand_fntn_info, year, cursor)
        connection.commit()
    print(f"{time.time()-start:.4f} sec") # 종료와 함께 수행시간 출력 -> 1000개 목록 조회 + DB저장 = 868.5183 sec
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()