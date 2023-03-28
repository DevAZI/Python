##따라서 hash를 이용한 문제풀이를 배워보도록 하자

def solution(phone_book): 
    hashMap = {}
    for nums in phone_book: #hash map 생성
        hashMap[nums] = 1
    
    for nums in phone_book: #phonebook의 문자열을 하나씩 받아옴
        arr= ""
        for num in nums: #하나씩 받아온 문자열을 하나씩 쪼개서  arr에 붙임
            arr += num
            if arr in hashMap and arr != nums: #그래서 해시맵에 있는 값과 그값이 일치할 경우 값을 반환함
                return False
    return True
#이게 결국 앞에서 부터 문자열을 추가하면서 동작하기 때문에 값이 중간에 같은 것이 있어도 상관없이 접두사만 같은 값일 경우에 작동







# 짜봤는데 테스트 케이스 2개 틀림 + 효율성 2개 ㅂ
# def solution(phone_book):
#     answer = True
    
#     phone_book.sort()
#     n = 0
#     while phone_book:
#         i = phone_book.pop(0)    
    
#         for n in range(len(phone_book)):
#             if phone_book[n].find(i) != -1:
#                 answer = False
#                 return answer
#             else : answer = True    
    
#     return answer
# a = list(input().split())
# solution(a)