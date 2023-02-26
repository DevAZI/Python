
#행렬 덧셈 , 곱셈은 크기가 같아야함
a, b = map(int, input().split())
arr1 = []
arr2 = []
for i in [arr1,arr2]:
    for j in range(a):
        i.append(list(map(int, input().split())))

for i in range(a):
    for j in range(b):
        arr1[i][j] += arr2[i][j]
    print(*arr1[i])


