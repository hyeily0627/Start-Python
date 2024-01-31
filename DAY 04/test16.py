# date : 2024-01-18  
# desc : 15. 예외처리(Exception handling) _2 

def add (x, y) :
    result = x + y
    return result

def minus(x, y) : 
    result = x - y
    return result

def divide(x, y) : 
    result = x / y
    return result

try : 
    a, b = map(int, input('두 숫자를 입력 >').split(' '))

    print('테스트 시작')

    print('더하기', add(a, b))
    print('빼기', minus(a, b))
    print('나누기', divide(a, b))

except :
    print('입력값이 잘못되었습니다.')
    print('정수 입력 또는 제수에 0을 입력하지 마세요')

# 함수 = 메서드 = 프로시저 = 서브루틴     

##예외처리 try except finally

