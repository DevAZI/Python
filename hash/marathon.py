def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    n = len(completion)
    for i in range(n):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
    
    
    return answer