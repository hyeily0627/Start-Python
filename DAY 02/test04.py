# date : 2024-01-16
# desc : 변수(지난시간부터 계속)
a = 100 
b = 200
print (a + b)

a = 23.67 # a변수의 값을 100에서 실수형 23.67로 변경
print (a + b)
# 계산 시 223.67000000000002으로 출력되는데, 이는 파이썬 오류(큰 영향 X)

a = 'hello'
b = 5
print(a * b)
# hello라는 문자를 5번 출력

a = False 
print(a)
# 거짓은 0, 참은 1
a = True 
print(a * b)

# 변수명은 의미있는 단어 조합으로 해야한다.
# 숫자 불가, 문자+숫자 가능, 특수문자 불가(_만 가능)
account_money = 300000
car_fuel = 34
cloth54 = '무스탕'
_test_value = 11

greeting1 = 'hello'
greeting2 = 'world'
print(greeting1, end=' ') # 엔터를 하지 않고, 마지막에 스페이스로 변경함
print(greeting2)

