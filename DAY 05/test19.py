# date : 2024-01-19
# desc : 파일 쓰기

f = open('./DAY 05/test02_txt', mode='w', encoding='utf-8')
# 밑에 터미널 보면 C:/Sources/Python_src까지만 있기때문에 DAY05부터는 작성

f.write('저는 한국사람입니다.\n')
f.write('저는 김치를 좋아합니다.')

f.close()