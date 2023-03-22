#dp 보다는 앞으로 다른 문제를 푸는게 실력에 향상될거라 생각해 일단 스탑
n = int(input())
arr= []
for i in range(n):
    arr.append(int(input()))

maxResult = arr[0]
for a in range(3, n -1):
    
    #maxResult = max(arr[a-2] + maxResult,arr[a-3]+maxResult arr[a-1]+ maxResult)  
    #3칸연속으로 하면 안되는거 짜야함
    print(maxResult)
maxResult += arr[-1] #마지막은 밟아야한다
print(maxResult)
