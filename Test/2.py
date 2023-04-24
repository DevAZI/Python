
#22
#값 순회하면서 max값 찾아서 값 저장하고, 첫 min 값 저장한다음에 그거랑 max min 차이값 저장하고, 해당 값 가장 큰거로 하면되지 않을까
a = int(input())
arr = list(map(int,input().split()))
arr.append(-1)
maxResult = arr[0]
minResult = arr[0]
result = 0
# for i in range(a):
#     minResult = min(minResult, i)   
    
#     if arr[i] >arr[i+1]:
#         maxResult = max(maxResult,i)
        
#         result = maxResult - minResult
    
# print(result)
resultMax = 0
#값이 낮아지는 부분 까지에서 min값이랑 max값이랑 비교하기
start = -1
for i in range(a):
    
    
    if arr[i] > arr[i+1]:
        #start를 만들어내야함지금

            


        minResult = min(arr[:i+1])      ##  여기 수정필요
        maxResult = max(arr[:i+1])      #여기를 값이 낮아지는 구간전부터 후까지 각 값을 해서 하면 될듯 [x:y]이런게 된다면 이런식으로 진행해보자


        print(f"min: {minResult}")
        print(f"max: {maxResult}")

        result = maxResult - minResult
        resultMax = max(resultMax, result)
print(resultMax)


    

