#대충 1~8 까지 인 [1~8]로 배열 9칸 짜리 배열 만들고, 
#연속되는거 카운팅 해서 최대값 해당 배열에 값 최신화하면서 넣으면 될것같은데.
maxCount = [0 for a in range(9)]
for _ in range(3):
    arr = list(map(int, input()))
    arr.append(-1)
    print(arr)
    count = 1
    for i in range(8):
        if arr[i] != arr[i+1]:
            maxCount[i+1] = max(maxCount[i+1], count)
            count = 1
        else: 
            count+=1        
    print(max(maxCount))    

#1. 하나씩 돌면서 같으면 카운팅
#2. 값이 달라진다면..? 그때 전 카운팅 값 최대값이랑 전에 숫자랑 비교해서 크면 최신화
#3. 근데 최대값보다 남은 숫자가 적으면 아닐태니까 그 이후 숫자는 이제 끊어도 되긴하겠다. (MAX > 남은 숫자) : CONTINUE


