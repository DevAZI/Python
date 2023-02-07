import math
a = int(input())
for i in range(a):
    arr = list(map(int, input().split()))
    j = 1
    totalSum = 0
    for j in range(arr[0]):
        totalSum += arr[j]
    print(round(totalSum/arr[0], 3))    


