#답지확인

#저번에 답지본거 같은데 기억이 안 남, 답지 안 보면 도저히 못풀듯..
#배열에있는걸 0 idx부터 차례대로 더하기 빼기를 넣는다?...
#뺐을때 idx+1을 넣어야하는데 순서 섞일수있으니 idx함께 넣는다? 

#직접 다시 안 풀어서 그런가
from collections import deque

#이게 그래프인지 생각 못할듯  
# 배열에서 더하거나 빼거나 두가지 노드를 반복해서 탐색
#dfs(스택 마지막넣은거 뺴도) bfs(큐 먼저넣은거 뺴도)둘다 상관없다 idx 값으로 다음 원소를 결정하기 떄문? 
#마지막에 넣었던것 빠지면 마지막 idx +1인거 뺴내서 더하겠지
#먼저넣은거 뺴면 먼저 넣은 idx의 +1인거 빼내서 더하겠지


def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append((numbers[0], 0))
    q.append((-1 * numbers[0], 0))
    
    while q:
        temp, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append((temp + numbers[idx], idx))
            q.append((temp - numbers[idx], idx))
        else:
            if temp == target:
                answer += 1
    return answer
