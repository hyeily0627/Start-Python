# date : 2024-01-18  
# desc : 리스트 문자열 연산(추가)


arr = [i for i in range(10)]
print(arr)

arr[4] = 56
print(arr)
print(len(arr)) #출력값 10

arr.append(17) #리스트 마지막에 17 하나 추가
print(len(arr)) #출력값 11 
print(arr)

arr.insert(3, 'seven') #3번째 위치에 'seven'문자열 삽입
print(arr)

arr2 = [1, 2, 3]

arr.extend(arr2) #arr + arr2 
print(arr)

arr3 = [1,3,9,7,5,2] 
arr3.sort() #정렬(오름차순, 작은 값 -> 큰 값)
print(arr3)
arr3.sort(reverse=True) #정렬(내림차순, 큰 값 -> 작은 값)
print(arr3)

