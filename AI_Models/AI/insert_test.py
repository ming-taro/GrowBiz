import pandas as pd

# A.csv를 UTF-8 인코딩으로 읽기
# EUC-KR 인코딩으로 A.csv 파일 읽기
df = pd.read_csv('hansung.csv', encoding='euc-kr')

# 파일을 다시 저장하는 경우
df.to_csv('hansung_utf8.csv', encoding='utf-8', index=False)
