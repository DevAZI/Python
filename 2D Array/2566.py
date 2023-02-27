# arr1 = []
# arr2 = []
# for i in range(arr1, arr2):
#     for j in range(9):
#         i.append(int(input().split()))
import sys
input = sys.stdin.readline

arr1 = []
for i in range(9):
    arr1.append(list(map(int, input().split())))    

maxIndex = max(map(max,arr1))
print(maxIndex)
for i in range(9):
    for j in range(9):
        if arr1[i][j] == maxIndex:
            print(f"{i+1} {j+1}")



