import requests
import pandas as pd
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import pymysql

load_dotenv()

url = "https://www.serve.co.kr/good/v1/map/getAtclDetail"

mysql_connection = pymysql.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'), 
    database="KB",
    charset='utf8'
)

def find_detail(atclNo, ctgryCd1):
    params = {
        'tabNo': 4,
        'atclNo': atclNo,
        'ctgryCd1': ctgryCd1
    }

    # GET 요청 보내기
    response = requests.get(url, params=params)

    # 응답 처리
    if response.status_code == 200:
        data = response.json()  # JSON으로 파싱
        print(data)  # 데이터 출력

        result_list = data.get("data", {}).get("resultList", [])

        if 'data' not in data or 'resultList' not in data['data']:
            return
        if 'data' not in data or 'resultOptionList' not in data['data']:
            return

        for result in result_list:
            detail = {
                "주소": result.get("addr"),
                "층수": result.get("flr1"),
                "방향": result.get("drcCd"),
                "관리비": result.get("mmMcost"),
                "건축물 용도": result.get("bldUsageCd"),
                "주차대수": result.get("parkCcnt"),
                "부동산 대표 번호": result.get("mdiatBzestRepTelno"),
                "공인중개사 전화번호": result.get("mdiatBzestRepMoblno"),
                "공인중개사 이름": result.get("mdiatBzestNm"),
                "매물설명": result.get("dtlDesc"),
            }
            
            # 난방(방식/연료) 추가
            result_option_list = data.get("data", {}).get("resultOptionList", [])
            heating_methods = [option.get("cdNm") for option in result_option_list]
            detail["난방(방식/연료)"] = heating_methods
            
            extracted_data.append(detail)

    else:
        print(f"요청 실패: {response.status_code}")

    try:
        if mysql_connection.open:
            print("Successfully connected to the database")

            # query = "SELECT main_category, sub_category, store_name, serial_number FROM BusinessInfo"
            mysql_cursor = mysql_connection.cursor()
            # mysql_cursor.execute(query)

            result = mysql_cursor.fetchall()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if mysql_connection.open:
            mysql_cursor.close()
            mysql_connection.close()
            print("MySQL mysql_connection is closed")

