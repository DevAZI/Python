arr = list(map(int,input()))
arr.sort()
for i in sorted(arr,reverse=True):
    print(i,end='')