# date : 2024-01-18  
# desc : 15. 예외처리(Exception handling) _1

def add (x, y) :
    result = x + y
    return result

def minus(x, y) : 
    result = x - y
    return result

def divide(x, y) : 
    try: 
        result = x / y
    except :
        print('제수는 0을 사용할 수 없음! ')
        result = 0
        
    return result

try : 
    a, b = map(int, input('두 숫자를 입력 >').split(' '))
except : 
    print('정수만 입력하세요.')
    a = 1
    b = 1   

print('테스트 시작')

print('더하기', add(a, b))
print('빼기', minus(a, b))
print('나누기', divide(a, b))

# 함수 = 메서드 = 프로시저 = 서브루틴     

##예외처리 try except finally

