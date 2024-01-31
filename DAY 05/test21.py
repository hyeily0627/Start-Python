# date : 2024-01-19 금요일  
# desc : csv 모듈사용 파일읽기

import csv

f =open('./DAY 05/busanbus_20221231.csv', mode='r', encoding='cp949')
reader = csv.reader(f, delimiter=',')
next(reader)
for line in reader:
    print(line)

f.close()

# https://notepad-plus-plus.org/downloads/ 메모장 (인코딩 변환)
# exel viewer 설치 = csv 파일 우클릭 - open preview 클릭시 엑셀창 처럼 확인가능 