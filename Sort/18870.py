#다시
cnt = int(input())

arr = list(map(int, input().split()))

print(arr) 

arr.sort(reverse=True)

#값이 같을경우
for i in range(cnt):
    if arr[i] == arr[i+1]:
        print(arr[i])
        continue
    else: print(arr[i])


