import math
a = int(input())
for i in range(a):
    arr = list(map(int, input().split()))
    
    avg = sum(arr[1:])/arr[0]
    cnt = 0
    for i in arr[1:]:
        if i > avg:
            cnt  += 1
    a = round(cnt/arr[0]*100,3)
    print('%.3f' % a + '%')
