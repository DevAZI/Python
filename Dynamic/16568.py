#아무튼 전체 N에서
#N - a, N - b하면서 가장 적은 min값을 찾는다고 생각하고
#근데 음수가 되지 않게 해야함

n, a, b = map(int, input().split())


result = 0
while n > 0:
    # if (n-a) > (n-b):
    #     n  = n -a
    #     result += 1
    # elif (n-b) > (n-a):
    #     n = n - b
    #     result += 1
    # else:
    #     n = n -1
    #     result += 1 
    result += 1
    n = min((n-a), (n-b), (n-1))
    
    #print(n)
print(result -1)

        
 
 