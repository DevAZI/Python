#KADANE
import sys
input= sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))


maxSum = arr[0]
currentSum = 0
for i  in arr:
    currentSum = max(currentSum + i, i)
    maxSum = max(maxSum, currentSum)   

print(maxSum) 
    


#몇개의 갯수를 이용했는지
# def maximum_subarray_sum(arr):
#     max_sum = float('-inf')
#     curr_sum = 0
#     start_idx = 0
#     end_idx = 0
#     curr_start_idx = 0
#     for i, num in enumerate(arr):
#         if num > curr_sum + num:
#             curr_sum = num
#             curr_start_idx = i
#         else:
#             curr_sum += num
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#             start_idx = curr_start_idx
#             end_idx = i
#     return max_sum, start_idx, end_idx

