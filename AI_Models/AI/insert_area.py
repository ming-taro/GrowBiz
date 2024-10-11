# import pandas as pd
# import pymysql
# import os
# from dotenv import load_dotenv

# # .env 파일에서 DB 정보 불러오기
# load_dotenv()

# DB_HOST = os.getenv("DB_HOST")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")

# # MySQL에 연결하기 위한 함수
# def connect_to_db():
#     return pymysql.connect(
#         host=DB_HOST,
#         user=DB_USER,
#         password=DB_PASSWORD,
#         db=DB_NAME,
#         charset='utf8mb4'
#     )

# # CSV 파일을 읽고 데이터를 업데이트하는 함수
# def update_area_from_csv(csv_file, table_name='all_district'):
#     # CSV 파일 읽기
#     df = pd.read_csv(csv_file)
    
#     # 필요한 컬럼만 선택
#     # 동별(2) -> gu_name, 동별(3) -> dong_name, 면적 (k㎡) -> area
#     area_df = df[['동별(2)', '동별(3)', '면적 (k㎡)']].copy()
#     area_df.columns = ['gu_name', 'dong_name', 'area']

#     # DB 연결
#     connection = connect_to_db()
#     cursor = connection.cursor()

#     # 각 행에 대해 면적 값을 업데이트
#     for idx, row in area_df.iterrows():
#         gu_name = row['gu_name']
#         dong_name = row['dong_name']
#         area = row['area']

#         # MySQL 테이블에서 gu_name과 dong_name을 기준으로 면적 업데이트
#         sql = f"""
#         UPDATE {table_name}
#         SET area = %s
#         WHERE gu_name = %s AND dong_name = %s;
#         """
#         cursor.execute(sql, (area, gu_name, dong_name))

#     # 변경 사항 저장
#     connection.commit()
#     cursor.close()
#     connection.close()

# # CSV 파일과 MySQL 테이블 업데이트 실행
# if __name__ == "__main__":
#     update_area_from_csv('행정구역(동별)_20241011154245.csv')
import pandas as pd

# CSV 파일에서 컬럼명 확인
df = pd.read_csv('hansung.csv')
print(df.columns)