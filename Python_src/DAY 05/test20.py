# date : 2024-01-19
# desc : csv(는 텍스트 파일) 엑셀파일 읽기

f = open('./DAY 05/busanbus_20221231.csv', mode='r', encoding='cp949')
# ./ = C:/Sources/Python_src 
# 파일 읽은 처리
text = f.read()
print(text)
f.close

# / 는 리눅스, 유닉스 방식이고 \는 윈도우 방식입니다. 
# 역슬래시는 Escape 문자이기 때문에 표현할때는 \\ 과 같이 써야합니다.
# 인코딩 방법 : ascii (영어만 처리), cp949(한글처리), utf-8

print('-------------------------------------')

f = open('./DAY 05/test.txt', mode='r', encoding='utf-8')

while True : 
    line = f.readline()
    if not line:
        break

    print(line)
f.close
# 한줄씩 읽어서 처리하고, 라인에 아무것도 없으면 빠져나옴