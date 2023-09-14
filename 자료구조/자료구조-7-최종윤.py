처음 풀이
``
from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    q = deque()
    total = 0
    i = 0
    t = 0
    while i < len(truck_weights):
        
        #꽉 찾을 때 마지막 들어온 것까지 빠져나갈려면 bridge_length
        #하나 더 들어올수 있을 때까지
        if total >= weight:
            t += bridge_length
            while total >= weight:
                tmp = q.popleft()
                total -= tmp
            print("after clear",q,t)
            total = 0

                # 100
                        # 10
            
        
        q.append(truck_weights[i])
        total += truck_weights[i]
        t += 1
        i += 1
        print("after append",q,t)
    
    if q:
        t += bridge_length
        q.clear()
        
    
    return t
``

답지 본 후
``
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    #다리 
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    while(bridge):
        answer+=1
        total_weight -= bridge.popleft()
        if(truck_weights):
            if(truck_weights[0] + total_weight <= weight):
                total_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer
``    
