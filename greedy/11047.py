a, b = map(int, input().split())
arr = []
for i in range(a):
    arr.append(int(input()))

count = 0
for i in reversed(range(a)):
    count += b//arr[i]
    b = b%arr[i]
print(count)
