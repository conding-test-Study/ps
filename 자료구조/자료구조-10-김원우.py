from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    
    q = []
    
    for food in scoville:
        heappush(q, food)
    
    while True:
        food = heappop(q)
        if food >= K:
            break
        elif len(q) == 0:
            # 마지막까지 음식 섞었는데도 음식의 스코빌지수 K를 못넘으면 -1
            answer = -1
            break
        else:
            tmp = heappop(q) # 두번째로 맵지않은 음식
            heappush(q, food + (tmp*2))
            answer += 1
    
    return answer
