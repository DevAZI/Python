n = list(input()) # 값 받아와용
max = int(n[0]) # 첫번쨰 값을 넣어줘요


for i in range(1, len(n)): #첫번쨰 값을 제외하고 길이 만큼 계속 반복해요
    num = int(n[i]) # 문자열로 값을 받아왔으니, 정수형으로 바꿔줄꺼에요
    if num <= 0 or max <= 0:    #값이 0이나오면 더해줘야해요, 곱하면 값들이 0이 되잖아요
        max += i
    else: 
        max = max *i
    
print(max)        