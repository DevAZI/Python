n = int(input())

arr = list(map(int,input().split()))
arr.sort()
dsum = 0
for i in range(1,n+1):
    dsum += sum(arr[0:i])
print(dsum)

