#1.속한 노래가 가장 많이 재생된 장르인지
#> 이것도 해시맵(Dic) 이용해서 하면 되겠다.
#2.장르내 많이 재생된 노래를 먼저 수록
#> 플레이 순서로 소팅해야것네
#3.장르내 재생횟수가 같은 노래는 고유번호가 낮은 노래를 먼저 수록
#> 이거는 일단 재생회수같은지는 나중에 하고, 고유번호와 각 장르를 dic으로 키값과 벨류로 해야할듯
#> 그럼 이중 DIc이 가능한가
#장르 : {고유번호 : 플레이횟수} 이렇게 하면 될것같을지도

def solution(genres, plays):
    #재생수 
    playCount = {}
    for i in range(len(genres)):
        if genres[i] in playCount:
            playCount[genres[i]]  += plays[i]
        else:
            playCount[genres[i]] = plays[i]
    

    print(playCount)

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
    
    