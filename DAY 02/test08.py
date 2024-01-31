# date : 2024-01-16  
# desc : 흐름제어 (if for while) 

name = '혜민'

if name == '혜진' : 
    print('진료실로 들어간다')
else :
    print('그대로 있는다')

# 다중조건문 : elif
if name == '혜진' : 
    print('진료실로 들어간다')
elif name == '용석' :
    print('주사실로 들어간다')
else :
    print('그대로 있는다')    

print('--------------------')

name = '혜진'
state = '몸살'

if name == '혜진' : 
    print('진료실로 들어간다')
    if state == '감기' :
        print('선생님 아파요')
        print('어디가 아프나요')
        print('기침이 심해요')
    elif state == '몸살' :
        print('선생님 아파요')
        print('오한이 듭니다')
elif name == '용석' :
    print('주사실로 들어간다')
else :
    print('그대로 있는다')    

print('--------------------')
name = '용석'
state = '몸살'

if name == '혜진' and state == '감기' :
    print('진료실로 가서')
    print('선생님 감기인거같아요. 약주세요.')
elif name == '혜진' and state == '몸살' :
    print('진료실로 가서')
    print('몸살인거같아요. 링겔 주세요')
elif name == '용석' and state == '몸살' :
    print('주사실로 가서')
    print('주사를 맞는다')
else : 
    print('대기하세요')
    
print('--------------------')
