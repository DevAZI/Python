a = int(input()) #테스트케이스 개수
for i in range(a):
    arr = list(input())    
    for j in arr[2:]:        
        print(j*int(arr[0]), end='')  
    print()
    
    
