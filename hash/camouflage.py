def solution(clothes):
    
    hash_map = {}
    for clothe, clothe_type in clothes: #옷 종류별로 정리하면서 , 각 종류의 옷들의 갯수를 늘림 , 없다면 0
        hash_map[clothe_type] = hash_map.get(clothe_type, 0) + 1
        
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for clothe_type in hash_map:   
        answer *= (hash_map[clothe_type] + 1)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))





