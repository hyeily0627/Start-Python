# date : 2024-01-16
# desc : 자료형 상세

## None 타입 : 값이 없다.(no empty, 0도 아님 - 0 또한 값임)
c = None
print(c == None)
print(c == 0)
# == 왼쪽/오른쪽이 같은가? 같으면 True /다르면 False

## 숫자 타입
galaxy = 100
print(galaxy)
print (type (galaxy))
galaxy = 10_000_000
print(galaxy)
galaxy = 3.1415926672
print(galaxy)
print (type (galaxy))

##진수
galaxy = 0b101011 #2진수
print(galaxy)
galaxy = 0o52 #8진수
print(galaxy)
galaxy = 0xf1 #16진수
print(galaxy)

##문자열형
bruce_eckel = 'Life is short, You need python'
print(bruce_eckel)
bruce_eckel = 'Life is short, \nYou need python'
print(bruce_eckel)

text = '''안녕하세요
저는 홍길동입니다.
건강하세요'''
print(text)

##불형 : 불린 boolean 참 (True,1), 거짓 (False,0) 
print(1 + 1 == 1)
print(2*15 == 30)
print(True is True)

c= False
print(c)
print(type(c))

##복합형(자료구조)
a1 = 1
a2 = 2
a3 = 3 
a4 = 4 
print(a1,a2,a3,a4)
#리스트 == 배열 [ ]
b = [1,2,3,4]
print(b)
print(len(b))

c = [i for i in range(1,5) ]
# 1부터 5사이의 숫자
print(c)

arr = [1, False, 'True', 3.14, [1, 3, 5, 7] ]
print(arr)

arr1 = [] #빈리스트
print(arr1)

print(b)
#b라는 리스트의 3번째 값을 30으로 변경
b[3] = 30
print(b)

##튜플(리스트와 값나열함은 같음) ( )
d = (1, 3, 5, 9)
#print(d)
#d[2] = 30 
#튜플은 들어있는 값 수정불가 'tuple' object does not support item assignment
#prion(d)

## 딕셔너리
dinc = { 'school' : '학교' , 'grade' : '학년' }
spiderman = { 'name' : 'peter', 'age' : 18, 'weapon' : 'web shooter' }
print(spiderman) 