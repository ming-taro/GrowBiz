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
    charset='utf8mb4',  # utf8mb4로 설정
    use_unicode=True
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

        result_list = data.get("data", {}).get("resultList", [])

        if 'data' not in data or 'resultList' not in data['data']:
            return
        if 'data' not in data or 'resultOptionList' not in data['data']:
            return

        for result in result_list:
            addr = result.get("addr")
            is_first_floor = 1 if result.get("flr1") == "1" else 0
            drc_cd = result.get("drcCd")
            mm_mcost = result.get("mmMcost")
            bld_usage_cd = result.get("bldUsageCd")
            park_ccnt = result.get("parkCcnt")
            mdiat_bzest_rep_telno = result.get("mdiatBzestRepTelno")
            mdiat_bzest_rep_moblno = result.get("mdiatBzestRepMoblno")
            dtl_desc = result.get("dtlDesc")
            
            # 난방(방식/연료)
            result_option_list = data.get("data", {}).get("resultOptionList", [])
            heating_methods = [option.get("cdNm") for option in result_option_list]
            heating_info = "null" if len(heating_methods) == 0 else ','.join(heating_methods)

            sql = "UPDATE property_listing SET addr = %s, is_first_floor = %s, drc_cd = %s, mm_mcost = %s, bld_usage_cd = %s, park_ccnt = %s, mdiat_bzest_rep_telno = %s, mdiat_bzest_rep_moblno = %s, dtl_desc = %s, heating_info = %s WHERE atcl_no = %s;"
            mysql_cursor.execute(sql, (addr, is_first_floor, drc_cd, mm_mcost, bld_usage_cd, park_ccnt, mdiat_bzest_rep_telno, mdiat_bzest_rep_moblno, dtl_desc, heating_info, atclNo))
    else:
        print(f"요청 실패: {response.status_code}")


def selectPropertyInfo():
    try:
        if mysql_connection.open:
            print("Successfully connected to the database")
            query = "SELECT atcl_no, ctgry_cd1 FROM property_listing"
            mysql_cursor.execute(query)
            return mysql_cursor.fetchall()
    except Error as e:
        print("Error while connecting to MySQL", e)

mysql_cursor = mysql_connection.cursor()

property_info = selectPropertyInfo()
batch_size = 1000

for index in range(0, len(property_info)):
    print(index, ":", property_info[index])
    find_detail(property_info[index][0], property_info[index][1])
    if (index + 1) % batch_size == 0:
        mysql_connection.commit()

mysql_connection.commit()
mysql_cursor.close()
mysql_connection.close()
print("MySQL mysql_connection is closed")