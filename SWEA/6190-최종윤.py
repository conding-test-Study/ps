from collections import deque
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    answer = -1
    
    for i in range(n-1):
        for j in range(i+1, n):
            tmp = data[i] * data[j]
            arr = list(map(int, list(str(tmp))))
            
            is_increment = True
            for k in range(len(arr) - 1):
                if arr[k] > arr[k+1]:
                    is_increment = False
                    break
                
            if is_increment:
                answer = max(tmp, answer)
                
    print("#{} {}".format(tc, answer))
