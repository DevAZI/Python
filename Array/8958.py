a = int(input())
for j in range(a):
    arr = list(input())    
    count = 0
    totalSum = 0
    for i in range(len(arr)):
        if arr[i] == "O":
            count += 1 
            totalSum += count            
        elif arr[i] == "X":
            count = 0
    print(totalSum)