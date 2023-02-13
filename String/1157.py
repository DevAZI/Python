a = input().upper() #입력   
  
b = []  
arr = set(a)    #중복 제거
arr= list(arr)  #리스트로 변경
maxCnt = []

for i in range(len(arr)):
    b.append(a.count(arr[i]))

if b.count(max(b)) >=2:
        print("?")
else : print(arr[b.index(max(b))])


    



