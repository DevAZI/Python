arr = []
for i in range(0, 9):
    arr.append(int(input()))
print(max(arr))
print(arr.index(max(arr))+1)


# fmax = max(arr)
# print(fmax)
# for j in range(0, 9):
#     if fmax == arr[j]:
#         print(j+1)
