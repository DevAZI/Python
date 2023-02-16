import sys
#import statistics
from collections import Counter
input = sys.stdin.readline

a = int(input())
arr = []
for i in range(a):
    arr.append(int(input()))

arr.sort(reverse=True)
print(sum(arr)/a) #평균
print(arr[a//2])#중앙값
#최빈값 다시
print(max(arr) - min(arr))#범위

# #평균
# print(round(statistics.mean(arr)))

# #중앙값
# print(statistics.median(arr))

# #최빈값 // 진짜 최빈값이네 이건..
# cnt = max(Counter(arr))
# print(cnt)

# #범위
# print(max(arr) - min(arr))