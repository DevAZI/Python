dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
a = list(input())
a.sort()
b= 0
countNum = 0
for i in range(len(a)): 
    for j in range(len(dial)):        
        if dial[j].find(a[i]) != -1:
            b += (j+2)                       
        else: continue

print(b+len(a))



