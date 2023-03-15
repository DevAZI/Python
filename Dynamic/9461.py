import sys
input= sys.stdin.readline

n = int(input())
arr= [1,1,1,2,2]
for j in range(5, 100):
    arr.append(arr[j -1] + arr[j-5])


for _ in range(n):
    a = int(input())
    print(arr[a-1])


