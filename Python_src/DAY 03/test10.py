# date : 2024-01-17  
# desc : 별표 찍기

# for i in range(6) : # 5가 아닌 6인 이유는 i = 숫자로 0부터 찍히니까 제일위에 공란으로 뜸
#     print ('*'*i)

# for i in range(1,6) : # 0 공란없이 시작
#     print ('*'*i)    

# ## range
# # range (n) 0부터 시작하는 범위
# # range (n, n+1) n부터 n+1 의 범위사이까지 

# print('-------------------------------------')

# ##이중 for문

# for i in range(1, 5+1) : 
#     for j in range(i) : 
#         print('*', end='')
#     print()

# print('-------------------------------------')    

# for i in range(1, 6) : 
#     for j in range(6 - i) : 
#         print('*', end='')
#     print()

# print('-------------------------------------')    

# for i in range(1, 6) : 
#     for j in range(i) : 
#         print('')
#     for j in range(i) :
#         print('*', end='')
# print()

for i in range(1, 6) : 
    for j in range(6-i) :  
        print(' ' , end='')
    for j in range(i) :
        print('*' , end='')
    print(' ')

# 강사님 풀이
for i in range(1, 6) : 
    for j in range(6-i) :  
        print(' ' , end='')
    for j in range(2*i-1) :
        print('*' , end='')
    print(' ')

#용석 풀이
for i in range(1, 6) : 
    for j in range(6-i) : 
        print(' ' , end='')
    for j in range(i) :
        print('*' , end='')
    for j in range(i-1) : 
        print('*' , end='')
    print(' ')

#으에에에에에엥
