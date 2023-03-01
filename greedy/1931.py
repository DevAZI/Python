#미완
cnt = int(input())
arr = []
arr2 = []
count =0
for i in range(cnt):
    arr.append(list(map(int, input().split())))

arr.sort()
for i in range(cnt):
    arr2.append(arr[i][1] - arr[i][0]) 
    
        
    


print(f"{arr} \n {arr2}")
print(count)



