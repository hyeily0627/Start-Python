# date : 2024-01-17  
# desc : 구구단

# x = 2

# for i in range(1, 10) :
#     print(x * i)

# x = 2

# for i in range(1, 10) :
#     print(x, 'x', i, '=', x*i)

# print('-------------------------------------')

# for x in range(2,10) : #2부터 9까지 
#     for i in range(1,10) : #1부터 9까지
#         print(x, 'x', i, '=', x*i) 

# print('-------------------------------------')

# for x in range(2,10) : #2부터 9까지 
#     print ('<', x, '단 시작 >')
#     for i in range(1,10) : #1부터 9까지
#         print(x, 'x', i, '=', x*i, end=' ') 
#     print('') #한줄 엔터
# print('구구단 끝!')

print('-------------------------------------')

##입출력방식으로 구구단 산출
# a = input('출력할 구구단 단을 입력하세요(숫자만) > ')
# a = int(a)  
# 위 두줄을 1줄로 만들면
# a = int(input('출력할 구구단 단을 입력하세요(숫자만) > '))

# for i in range(1,10) :
#     print(a, 'x', i, '=', a*i, end=' ')

# print('')    

print('-------------------------------------')

a = int(input('2단부터 출력할 마지막 단을 입력하세요(숫자만) > '))

for x in range(2, a+1) :
    print(x, '단 시작')
    for i in range(1,10) : # 1~9계산 완료
        # print(x, 'x', i, '=', x*i, end=' ')
        print(x, 'x', i, '=', f'{x * i:2}', end='\t')
        # 터미널창 라인 정렬 f'{x * i:2}

    print('')  # 한 줄 엔터

print('구구단 끝!')
