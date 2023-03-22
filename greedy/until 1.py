import math
import time
##시간 측정
start = time.time()

n, k = map(int, input().split()) # 값 입력
result = 0 #횟수 측정용 
while True:
    target = (n//k) * k # n이 k로 나누어 떨어지지 않을때 가장 가까운 숫자로 만들어줌
    result += (n- target) #그래서 그 효과가 n - 1 한 숫자임
    n = target # 그 가장 가까운 숫자로 n 
    ## 따라서 n -1의 연산 횟수를 줄이는 효과를 가질 수 있음
    
    if n < k:
        break
    result += 1
    n //= k
result += (n-1)
print(result)



##시간 측정
end = time.time()
print(f"{end - start:.5f} sec")






#88651621635484696 3






## 내가 짠 효율 좋지 않은 코드
# a, b= map(int,input().split())
# count = 0
# while a != 1:    
#     if a % b == 0:
#         a  = a // b
#         count += 1
#     else : 
#         a -= 1
#         count += 1
    
# print(count)
