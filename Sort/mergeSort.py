def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) //2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)
    return merge(leftHalf, rightHalf)
def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else : result.append(right.pop(0))
    
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))