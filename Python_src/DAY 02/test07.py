# date : 2024-01-16  
# desc : 연산자(operate)

# 2 = 1 #오류
# a == 1 #오류

import math
#1. import math as m : math를 m으로 짧게 호출하겠다. 
#2. from math import pi, sqrt, pow : math 에서  pi, sqrt, pow만 사용
#위와 같은 경우  pi, sqrt, pow 이거만 쓰면 호출 가능

print( 5 / 2 )
print( 5//2 ) #소수점 밑으로 절삭
print( 5%2 ) #나눈 나머지 값

print( 2 ** 10 ) #2의 10승
print(math.pow(2, 10))



## ( )
print( ( 3 + 5 ) * 10 )
print( 3 + ( 5 * 10 ) )

print('---------')

##문자열 연산 : + 와 * 만 지원
# + : 문자열 합치기
# * : 문자열 반복출력
g = 'hello' # 헬로와 월드사이에 여백주고 싶으면 'hello '
h = 'world'
print( g + h ) 
print( g * 5 )

print(g[0])
# g[0]= ' h '  
# print ( g ) 불가능

print(len(g))

## (문자열)리스트 자르기
print( g[0] )
print( g[0:4] )
print( g[2:5] )
print( g[-1]) # 뒤에서 부터 문자열 세어서 출력
print( g[-2:5]) # 출력값 lo (모르겠숴)

## 날짜/시간 문자열로 자르기 연습
curr_datertime = '2024-01-15 15-08-15'
print(curr_datertime[0:4] + '년') 
print(curr_datertime[5:7] + '월')
print(curr_datertime[9:10] + '일')
print(curr_datertime[17:] + '초') #마지막 인덱스를 적지 않으면 끝까지 표시

#리스트 자를때 뒤의 인덱스는 찾고자 하는 인덱스의 +1 해야함
arr = [2, 4, 6, 8, 10]
print(arr[1:3])

#리스트 합치기, 2배로 늘리기
arr2 = [1, 3, 5]
print(arr + arr2)
print( arr * 2 )

