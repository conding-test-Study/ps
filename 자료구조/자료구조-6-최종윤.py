틀린 풀이
from collections import deque

	def solution(prices):
    answer = [0] * len(prices)
    
    q = []
    out = 0
    for i in range(len(prices)):
        q.append((i, prices[i]))
        if i == (len(prices) - 1):
            break
        if prices[i + 1] < prices[i]:
            while q[-1][1] > prices[i + 1]:
                answer[q[-1][0]] = i + 1 - q[-1][0] 
                out += 1
                q.pop()
                
    
    
    k = 0    
    i = 0
    while i < len(q):
        if answer[i] == 0:
            answer[i+k] = len(q) - 1 - q[i][0] + out
            i += 1
        else:
            k += 1
    #1 2 3 3
    return answer
    #2빼고 1까지 idx차이 3뺴고 1까지 idx차이? out+1?        중간에 있는걸 빼버리면 오래걸릴텐데 뺴지 않고 answer만 저장? 
	#2의 idx를 어떻게아는데 그러면 차라리 이렇게 반복문 돌리는게 낫겠따 근데 얼마나? o(n)을 n번해야할수도 있는데?
	#인덱스도 같이 저장? 어 그러면 빼서 인덱스 가지고 i+1이랑 차이 구하면 되겠네 !!!!

답지 참고 후 
```
from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    q = []
    
    
    for i in range(len(prices)):
        while q and (prices[q[-1][0]] > prices[i]):
            idx, val = q.pop()
            answer[idx] = i - idx
        q.append((i, prices[i]))
    

    for i in range(len(q)):
        answer[q[i][0]] = len(prices) - 1 - q[i][0] 
        
    return answer
```

스택에 인덱스만 넣었고 answer[idx] = i - idx 
의사코드는 비슷하게 했던 것 같은데 
q.pop의 순서가 달르고 더 작은게 나와서 pop했을 때 
arr 끝 인덱스 에서 큐e의 인덱스를 뺴면 된다는 관계를 생각하지 못했다...
스택할때 그림을 그려놓고 관계식을 보는데 코드로 하기는 약간 불편한듯
종이 하나 있으면 편할것같기도하다 익숙해진다면
음 그려도 몰랐나? 큐 예시 그림만이 아니라 
관계를 볼때 원래있던 prices arr를 생각하지못했다


왜 시간초과됐지? pop된 e의 수를 세서  out에 저장
큐 인덱스 끝에서 큐 e의 인덱스를 빼고 out를 더하면 된다고생각했는데..


큐에 넣었던 것의 인덱스 idx를 answer[idx] 에 prices의 길이와 차를 넣으면됐는데 
그냥 반복문의 인덱스를 통해서 넣으려고 하다보니 복잡해진것같다..
