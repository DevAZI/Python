# 짜봤는데 테스트 케이스 2개 틀림 + 효율성 2개 ㅂ
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    n = 0
    while phone_book:
        i = phone_book.pop(0)    
    
        for n in range(len(phone_book)):
            if phone_book[n].find(i) != -1:
                answer = False
                return answer
            else : answer = True    
    
    return answer
a = list(input().split())
solution(a)
