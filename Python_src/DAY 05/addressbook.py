# date : 2024-01-18 목요일  
# desc : 주소록 프로그램

# [직육면체] - 하늘색으로 표현되는건 변수임
# 구문 잡고 ALT키 + 방향키 이동가능
# 명령프롬프트 = 콘솔 = 터미널

import os

def clear() : #콘솔(터미널 또는 명령프롬프트) 클리어(다 지우는) 하는 함수
    command = 'clear' # os 윈도우 : cls / linux, unix, mac : clear 명령어 사용 
    if os.name in ('nt','dos') : # 윈도우면
        command = 'cls'

def set_contact(): #연락처 입력 함수
    try : 
        name, phone, mail, address = input('입력(이름/폰번호/이메일/주소) >').split('/')
        set_contact = [name, phone, mail, address]
        return(set_contact)
    except : 
        return None # 오류발생했으니 none 으로 리턴 
    
def get_contact(lst) : #연락처 출력
    for item in lst:
        # print(item)
        for i in item: 
            print(f'{i}\t', end='')
        print('')

def chk_del_contact(name,lst) : #연락처 확인
    del_index = 0 
    for item in lst : 
        if item[0] == name:
            return del_index
        else:
            del_index += 1

def save_contact(lst) : #연락처리스트 파일 저장
    f = open('contact_db.txt', mode='w', encoding='utf-8')
            #경로 미지정시 어디에 저장 될까? 
            #c:/sources/python_src          
    for item in lst:
        f.write(item[0] + ',')
        f.write(item[1] + ',')
        f.write(item[2] + ',')
        f.write(item[3] + '\n')

    f. close

def load_contact(lst) : #실행시 연락처 로드
    f = open('contact_db.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline() #한줄씩 읽음
        if not line: break #반복문 탈출

        lines = line.replace('\n', '').split(',') 
        #쉼표로 분리된 길이 4 리스트 라인 생성. replace() 교체 \n을 ''
        contact = [lines[0], lines[1],lines[2],lines[3]]
        lst.append(contact)

    f. close 

def run() : #프로그램 실행함수
    lst_contact = []
    load_contact(lst_contact)
    # address = ['오혜진', '010-7696-1487', 'hj_o5h@naver.com', '부산']
    # print(address)
    # set_contact()
    lst_contact = [] 

    while True: #무한루프
        menu_num = show_menu() # 1,2,3,4
        if menu_num == 1: #1. 연락처 추가
            clear()
            contact = set_contact()
            if contact != None:
                lst_contact.append(contact)
            else : 
                continue
        elif menu_num == 2: #2. 연락처 출력
            clear()
            get_contact(lst_contact) 
        elif menu_num == 3: #3. 연락처 삭제
            clear()
            name = input('삭제할 이름 입력 > ')
            del_num = chk_del_contact(name, lst_contact)
            if del_num != None : 
                lst_contact.pop(del_num)
        elif menu_num == 4: #4. 종료라면
            save_contact(lst_contact) #종료직전 파일저장
            break #무한루프를 빠져나감
        else: 
            clear()

def show_menu() : #메뉴표시함수
    str_menu = ('주소록 프로그램 v0.2\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)
    try:   
        num = int(input('메뉴입력 : '))
        return num
    except : 
        return 0 #0으로 리턴 시키니까 다시 프로그램 메뉴 표시로 돌아감 

if __name__ == '__main__':
    run() 

print('프로그램을 종료합니다.')

