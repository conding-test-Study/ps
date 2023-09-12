
L개 범위 (윈도우)에서 최솟값을 구해보자 
윈도우에 대해 알아봤을 때 ,범위에서 합의 최대 최소를 구할 때 중복연산을 제거하기 위해 첫 인덱스에서 범위 합을 구한다음 한칸씩 이동하면서 범위 합을 계속 계산하지 않고 하나씩 더하고 빼서 효율화 한다는 점을 봤었는데

최소값을 구할 때는 한칸을 이동하고나서 기존의 최소값과 비교해서 다시 구하는데 최소 값이 범위 벗어났을 때 두번째 최소값과 새로 들어온 거를 비교하면서 효율화가 되지 않는다. 두번 쨰 최소값도 저장할 수 있다면 풀수 있을것 같은데 
정렬은 시간초과 발생할 것 같고 방법을 못 떠올렸다.
이 부분에서 스택 큐를 활용하여 하지 못해서 풀지 못한듯 하다.

처음 윈도우만 검색해보고 푼 풀이 (시간 초과)
``

N, L = map(int,input().split())
arr = list(map(int,input().split()))

window_min = arr[0]
min_idx = 0


for i in range(0, N):
    if i >= L:
        if min_idx <= i - L:
            # L개에서 최소 구하는 O(n)이 배열 N크기에서 반복돼서 O(n^2)
            window_min = min(arr[i-L+1 : i+1])
            if window_min == arr[i]:
                # 최소 값이 윈도우 벗어난 걸 알기 위한 idx
                min_idx = i
        else:
            window_min = min(arr[i], window_min)
            if window_min == arr[i]:
                min_idx = i
    else:
        window_min = min(arr[i], window_min)
        if window_min == arr[i]:
            min_idx = i
    print(window_min, end=' ')
    
``

저번에 빌딩 문제를 볼 때도 실제 예시를 손으로 써가며 넣고 빠지는 값을 확인해서 문제를 이해했었는데 이 문제도 스택 큐라 그런지 비슷한 것 같다.

최소 값이 범위를 벗어나는지 알기 위해 인덱스를 같이 저장 ㅇ
근데 답지에선 idx, val를 튜플로 저장했다 큐에다가.
스택 큐할 때 항상 앞에서 꺼낼때 큐를 쓰도록 떠올리기 !
합 구할 때처럼 끝 인덱스를 배열 크기 까지 윈도우 내에서 탐색 ㅇ

최소 값의 인덱스idx가 idx <= i-L인 경우 윈도우 벗어난 것이므로 
popleft해야한다. 최소 값은 가장 왼쪽에 있으므로
더 작은 것이 들어왔을 때 기존 들어있는 걸 빼고 넣기 때문



from collections import deque


N, L = map(int,input().split())
arr = list(map(int,input().split()))

q = deque()

for i in range(0, N):
    if q and q[0][0] <= i - L:
        q.popleft()

    while q and q[-1][1] > arr[i]:
        q.pop()

    q.append((i, arr[i]))
    print(q[0][1], end=' ')
    

