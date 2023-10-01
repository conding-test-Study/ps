# 로직을 떠올리는건 어렵지 않으나 구현할게 많아서 귀찮은 문제.
# 실제 코테에서 만나면 구현할 로직들을 빠르게 떠올려 정리한 후 구현하는 것이 시간절약에 도움이 될듯함

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
f = [[] for _ in range(n**2+1)] # 좋아하는 친구 리스트
room = [[0]*(n+1) for _ in range(n+1)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def find(room, friends):
    arr = []
    for i in range(1,n+1):
        for j in range(1, n+1):
            fr_cnt = 0
            va_cnt = 0
            if room[i][j] != 0:
                continue
            for k in range(4):
                new_i = i + di[k]
                new_j = j + dj[k]

                if 1 <= new_i <= n and 1 <= new_j <= n:
                    if room[new_i][new_j] in friends:
                        # 인접칸에 좋아하는 친구 있음
                        fr_cnt += 1
                    elif room[new_i][new_j] == 0:
                        # 인접칸 비어있음
                        va_cnt += 1
            arr.append([fr_cnt, va_cnt, i, j]) # [좋아하는 친구가 있는 인접자리, 빈자리수,i,j]
            # 비어있는 모든 자리에 대해 인접한 빈자리와 친구가 있는 인접자리를 탐색하여 배열로 만듦
    return arr

order = [] # 자리 배치할 순서
for i in range(n**2):
    tmp = list(map(int,input().split()))
    order.append(tmp[0])
    del tmp[0]
    f[order[-1]] = tmp # 좋아하는 친구 리스트 입력
### 입력받기

for i in range(1, n**2+1):
    arr = find(room, f[order[i-1]])
    # arr = [좋아하는 친구가 있는 인접자리, 빈자리수, i, j]
    arr.sort(key=lambda x : (x[0],x[1]), reverse=True) # 리턴받은거 조건에 맞게 정렬하기

    for target in arr:
        if room[target[2]][target[3]] == 0:
            room[target[2]][target[3]] = order[i-1]
            # 비어있는 자리면 바로바로 넣어버리기
            break

total_score = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        f_cnt = 0
        cur = room[i][j] # 좌석에 앉아있는 놈
        for k in range(4):
            new_i = i + di[k]
            new_j = j + dj[k]

            if 1 <= new_i <= n and 1 <= new_j <= n:
                if room[new_i][new_j] in f[cur]:
                    # 좋아하는 친구가 인접해있음
                    f_cnt += 1

        if f_cnt == 1:
            total_score += 1
        elif f_cnt == 2:
            total_score += 10
        elif f_cnt == 3:
            total_score += 100
        elif f_cnt == 4:
            total_score += 1000
print(total_score)