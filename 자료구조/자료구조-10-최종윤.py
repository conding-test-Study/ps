일부 테케만 통과
가장 작은 값과 두번째 작은 값 연산한걸 가지고 다시 두번째 작은 값이랑 연산하는데 .. 왜 힙을 쓰는거야? 가장 작은걸 계속 가져올수있으니까? 
근데 이렇게 해도 되는거 아닌가? 왜 틀린겨? 효율성에서만 틀린게 아니라 그냥 정확성이 틀리는데

작은 값을 뽑아오는데서 틀렸나? heapq쓰니까 되는거 보면 그런거 같긴 한데..
정렬된상태에서 계속 앞에서 뽑아오는데 그것을 tmp와 계속 연산하는데
두번쨰 작은 값을 구분하는데 문제있나? 계속 비교해줬는데?

다른 것 보고있다가 갑자기 떠올랐는데 연산하고 나온 결과가 가장작은 두번째 작은것이 아닌 것일수있다..
    13 7 9 면  그리고 K 가 10이면  13하고 7을 가지고 연산을 하는게 아니라 9를 가지고 연산을 해서 그렇다..
예시만 보고 그대로 하려고해서 그런듯 문제의 이해가 부족했다. 가장작은 두번째 작은걸 계속 뽑는다는 점에서 앞으로 최소힙을 이용하면 좋을것 같다.
13을 다시 정렬을 해야 제대로 되는데 그게 더 오래걸릴듯?
nlogn이 정렬이고 heappop이 logn상당히 빠르네 트리라 그런가 heapify가 n


풀이1 (정확성,효율성 실패)
``
from collections import deque

def solution(scoville, K):
    answer = 0
    
    scoville.sort()
    q = deque(scoville)
    
    
    tmp = q.popleft()
    while q and tmp < K:
        answer += 1
        
        tmp2 = q.popleft()
        if tmp < tmp2:
            tmp = tmp + tmp2 * 2
        else:
            tmp = tmp2 + tmp * 2
        
    q.appendleft(tmp)    
    
    if q[0] < K:
        return -1
    return answer
``    

35
``
from collections import deque
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        answer += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        
    
    
    if scoville[0] < K:
        return -1
    return answer
``    
