# date : 2024-01-17  
# desc : 14. 입출력

##사용자 입력 - 단일입력
# a = input('정수를 입력하세요. > ') 

# print(a * 3) # 결과물은 101010 

# print ('-----------------------------------')

# a = input('정수를 입력하세요. > ') 
# a = int(a) 

# print(a * 3) # 결과물은 30

##다중입력
# x, y, z = input('영단어 세 개를 입력하세요. > ').split(' ') #구분자를 줘서 자르기

# print('첫 번째 단어', x)
# print('두 번째 단어', y)
# print('세 번째 단어', z)

# x, y = input('영단어 두 개를 입력하세요. > ').split(',') #구분자를 줘서 자르기

# print('첫 번째 단어', x)
# print('두 번째 단어', y)

## escape 문자
print ('hello,\nworld\tI\'m Hugo!\b!')

##문자형 포맷팅 
name = '오혜진'
age = 20
gender = '여'       
print('안녕하세요. 저는 %s 입니다. 저는 %d대 입니다. %s자 입니다.'%(name, age, gender))

print('안녕하세요. 저는 %s 입니다. 저는 %4d대 입니다. %s자 입니다.'%(name, age, gender)) 
# %뒤 숫자 넣으면 크만큼 공백

print('안녕하세요. 저는 %20s 입니다. 저는 %3.3d대입니다. %s자입니다.'%(name, age, gender)) 
# %뒤 .숫자는 그 자리만큼 0 숫자표시 

print('-------------------------------------')

print('안녕하세요. 저는 {0} 입니다. 저는 {1}대 입니다. {2}자 입니다.'.format(name, age, gender)) 
print(f'안녕하세요. 저는 {name} 입니다. 나는 {age:4}대 입니다. {gender}자 입니다.') 
# {문자:숫자} 숫자만큼 공백


print('%4.4f'%(245.122222222222225))
print('%f4'%(245.122222222222225))
# 부동소수 ㅁ르겠숴요 
