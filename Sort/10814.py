import sys
input = sys.stdin.readline

cnt = int(input())
arr = []
for c in range(cnt):
    a, b = input().split()
    arr.append(((int(a),b,c)))


arr.sort(key = lambda x:x[2])
arr.sort(key = lambda x:x[0])

for i in range(cnt):
    print(f"{arr[i][0]} {arr[i][1]}")




