#미완
arr = ["c=", "c-","dz=","d-","lj","nj","s=","z="]
a = input()
count =0
for i in range(len(arr)):
    if a.find(arr[i]) != -1:
        a= a.replace(arr[i], '')      
        count +=1
print(count)
print(a)
print(count+len(a))