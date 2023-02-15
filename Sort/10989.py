#Counting Sort
import sys
input=sys.stdin.readline #input을 이용하면 시간이 더 걸리기에 
a = int(input())
arr = [0 for _ in range(10001)] #10000까지만의 숫자가 나오기에 미리 지정

for _ in range(a):  
    num = int(input())  #값 들어오는 것들 넣기
    arr[num] +=1    # 입력 받는 값들을 각 리스트에 카운트 1 추가
for i in range(1, 10001):
    count = arr[i]  #리스트 내에 각 숫자마다 몇개씩 
    for _ in range(count):#그 수만큼 해당 숫자 출력
        print(i)