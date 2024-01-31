# date : 2024-01-17  
# desc : 11. 함수 / 계산기

# 값을 반환한다 = return

def plus(x, y) : #int 
    result = x + y 
    return result

def minus(x, y) : #int 
    result = x - y
    return result

def mutlple(x, y) : #int 
    result = x * y
    return result

def devide(x, y) :  #float
    result = x / y
    # return result #만약에 주석처리하면 아래 구문 결과는 '나누기 결과는 None 입니다.'으로 뜸

# 매개변수 개수가 일정치 않은 경우(변수가 몇 개든 상관없이 더하는 함수) 
def adds(*params) : 
    result = 0
    for i in params : 
        result += i 
        # => result = result + 1 를 위와 같이 간단히 표현
    return result 

input('두 숫자를 입력하세요 > ').split(' ')

print (f'adds(1,2,3,4)') # = (adds(1,2,3,4))
print (f'adds(1,2,3,4,5,6,7,8,9,10)') # = (adds(1,2,3,4,5,6,7,8,9,10))
 

# a, b = input('두 숫자를 입력하세요 > ').split(' ')
# # a, b= int(input)('두 숫자를 입력하세요 > ').split(' ') 는 사용불가
# # 스플릿트에서는 묶어서 사용 불가
# # map(int, input)('두 숫자를 입력하세요 > ').split(' ')는 사용가능 - 이렇게 쓰면 밑에 구문 두개 삭제
# a = int(a)
# b = int(b)

# res = plus(a, b)
# print (f'더하기 결과는 {res}', '입니다.')
# print (f'더하기 결과! {plus(a, b)}', '입니다.')
# # 첫 번째줄은 변수로 리턴, 두 번째줄은 함수 호출하여 결과값으로 리턴 
# res = minus(a, b)
# print (f'빼기 결과는 {res}', '입니다.')
# res = mutlple(a, b)
# print (f'곱하기 결과는 {res}', '입니다.')
# res = devide(a, b)
# print (f'나누기 결과는 {res}', '입니다.') # 값을 0으로 나눌 수는 없음

# #매개변수 개수가 일정치 않은 경우 

