#답지확인  밑에 처음 풀이
import sys
from collections import defaultdict

# n : 회전 초밥 벨트에 놓인 접시의 수
# d : 초밥의 가짓수
# k : 연속해서 먹는 접시의 수
# c : 쿠폰 번호
n, d, k, c = map(int, sys.stdin.readline().split())

# 초밥 접시 상황
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 구간 인덱스 초기화
left, right = 0, k-1

# 구간 내의 접시 종류별 개수
dict = defaultdict(int)

# 구간 내에는 항상 쿠폰 번호가 포함되어있다고 가정
dict[c] += 1

# 첫 시작 구간의 접시 종류별 개수 저장
for i in range(right+1):
    dict[arr[i]] += 1

# 구간 내의 최대 접시 종류 개수 초기화
result = -int(1e9)

# 슬라이딩 윈도우 진행
while left < n:

    # 현재 구간 내의 접시 종류 개수와 최대 접시 종류 개수를 비교
    result = max(len(dict), result)

    # 윈도우를 오른쪽으로 한 칸씩 이동하기 위한 작업 진행

    # 현재 구간 내의 가장 왼쪽 접시를 제거
    dict[arr[left]] -= 1
    # 이제 해당 종류의 접시가 남아있지 않다면, 딕셔너리에서 제거
    if (dict[arr[left]] == 0):
        del dict[arr[left]]
    # 왼쪽 인덱스를 오른쪽으로 한 칸 이동
    left += 1

    # 오른쪽 인덱스를 오른쪽으로 한 칸 이동
    right += 1
    # 현재 구간 내의 가장 오른쪽 접시를 추가
    dict[arr[right % n]] += 1

# 결과 출력
print(result)


# 처음 풀이
import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = []
for i in range(n):
    belt.append(int(input()))

#belt sliding window k
tmp = deque()
cnt = 0
for i in range(4):
    if belt[i] not in tmp:
        cnt += 1
    tmp.append(belt[i])

max_cnt = cnt

max_list = []
max_list.append(tmp)
for i in range(4, n):
    val = tmp.popleft()
    if val not in tmp:
        cnt -= 1
    print(val, cnt)

    if belt[i] not in tmp:
        cnt += 1
    print(belt[i], cnt)
    tmp.append(belt[i])

    if max_cnt < cnt:
        max_list = tmp
        max_cnt = cnt
    elif max_cnt == cnt:
        max_list.append(tmp)

for i in range(k):
    val = tmp.popleft()
    if val not in tmp:
        cnt -= 1

    if belt[(n + i) % n] not in tmp:
        cnt += 1
    tmp.append(belt[(n - 1 + i) % n])

    if max_cnt < cnt:
        max_list = tmp
        max_cnt = cnt
    elif max_cnt == cnt:
        max_list.append(tmp)
      
#여러개 리스트 있는 max_list에서 c값이 있는지 list를 순회해야함
isC = False        
for tmp in max_list:
    if c not in tmp:
        isC = True
if isC:
    max_cnt += 1
print(max_cnt)
    
#belt[i:i+k]
# loop instead slicing -> (i + k) % n

#s,e를 따로 두니 e가 n을 넘어간 경우 처리가 쉬움
#s가 n-1까지 while로 하니 더 짧아짐

#defaultdict를 사용하니 리스트에 있는 값의 종류를 세는데 쉽네
#c가  list에 있는지 확인해서 max_cnt를 따로 셀 필요 없이  그냥 c 추가해 놓아도 상관이 없어지네
#max_cnt일 때 무슨 값들이었는지 list에 저장할 필요가 없네
#여러개 리스트 있는 max_list에서 c값이 있는지 list를 순회해야함

#전에 오답노트 정리 안 했더니 defauldict사용 못해서 복잡해진듯
#코드 복잡해지니 고려 못 한 것도 늘어나지 않을까?
#함수 단위로 작성해야하나.. 그러면 합치는 것도 배워야 하는데
#주석 많이 활용하는 것이 좋아보임 까먹는다.
