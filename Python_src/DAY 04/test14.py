# date : 2024-01-18 목요일  
# desc : Lottery 로또
 
import random

numbers = [i for i in range(1,46)] # 1~45까지 리스트
Lottery = []

for i  in range(6) : # 6번 돌면서 
    Lottery.append(random.choice(numbers)) # 1~45 중 하나를 뽑아 LOTTO에 담음 

print(Lottery)

print('-------------------------------------')
