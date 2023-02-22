import sys
input = sys.stdin.readline
a = int(input())
arr = []
input1=0; input2 = 0
for _ in range(a):
    input1, input2 = map(int,input().split()) 
    arr.append((input2,input1))
arr.sort()
for i in range(a):
     print(f"{arr[i][1]} {arr[i][0]}")

