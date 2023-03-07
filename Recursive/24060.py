#미완
def merge_sort(arr):    
    if len(arr) <= 1:   
        return arr  # 요소가 1개 이하인경우 이미 정렬 되있기에 반환

    mid = len(arr) // 2     
    left_half = arr[:mid]   #왼쪽 이랑 오른쪽으로 나눠서 그냥 가운대를 나눠서 만듬
    right_half = arr[mid:]

    left_half = merge_sort(left_half)  
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)     #왼쪽과 남

def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result 