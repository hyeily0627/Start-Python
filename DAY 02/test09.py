# date : 2024-01-16  
# desc : 반복문 (for 문 / while 문) 

## for 문
arr = [1,2,3,4,5,6,7,8,9,10]

for i in arr : 
    print (i)
# arr에 있는 i갯수(10개)만큼 반복하여 출력
# 인덱스 번호가 아닌 인덱스 원래 숫자를 출력
    
print('-------------------------------------')

arr = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for i in arr : 
    sum = sum + i
    # print (i)

print ('합계는', sum)
print ('출력완료!')

print('-------------------------------------')

arr = [i for i in range(1, 101, 2)] #100 + 1 , 2 홀수만?   
sum = 0  

for i in arr : 
    sum = sum + i
    # print (i)

print ('합계는', sum)
print ('출력완료!')

print('-------------------------------------')

## while 문 : for 과 같은 반복이지만, 종료위치를 정할 수 있음
hit = 0 

while hit < 10: #while은 이러한 조건을 잘 정해줘야지 TRUE 등으로 지정하면 무한루프임 (종료 CTRL + C 2번)
    hit = hit + 1

    if hit == 10:
        print('10번 찍어 나무가 넘어갔습니다.')
    else :
        print(hit, '번 나무를 찍었습니다.')

print('나무 찍기 완료!') #만약에 while 조건을 잘못적어서 해당 구문까지 도달 불가하면 연하게 글씨가 나타남. 

print('-------------------------------------')

STAR = ['*']

for i in range(1,6) : 
    print ('*'*i)

print ('출력완료!')

for i in range(6) :
    print ('*'*i)