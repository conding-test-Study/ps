#답지확인
from sys import stdin
from collections import defaultdict

def solution(N, K, A):
    answer = 0
    start, end = 0, 0

    # [1] 수열에 주어진 각 정수의 개수
    numberCount = defaultdict(int)

    # [2] 투 포인터
    while end < N:
        if numberCount[A[end]] >= K:
            numberCount[A[start]] -= 1
            start += 1
        else:
            numberCount[A[end]] += 1
            end += 1
            answer = max(answer, end - start)

    return answer

# input
N, K = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))

# result
result = solution(N, K, A)
print(result)


#answer로 구하는게 뭔지 해깔림
#- 반복문 내내 right - left 로 최대 증가 부분 수열의 길이를 갱신한다.
# left가 가리키는 숫자가 K개 미만으로 나왔을 때 right를 증가시켜 범위를 확장한다.
#end가 k 개 이하일떄 end를 증가시킨다고 생각했는데 k개가 됐을때 end+1 돼고 다음 end에서의 cnt를 세니까 
# 다음에 그 k개 있는 문자 나왔을때  감소시킨다음 적용해야함
#max_cnt저장하지 않고 end의 값이 k이상 나왔으면 s증가시키다 k보다 작아지면 end에 있는거 반영하고 +1  

while s <= e < n:
    # max_cnt <= k 면 cnt세고 
    if max_cnt <= k:
        cnt[data[e]] += 1
    # max_cnt보다 큰게 나오면 갱신 
        if cnt[data[e]] > max_cnt:
            max_val = data[e]
            max_cnt = cnt[data[e]]
    #e를 증가시킨다.
        e += 1
        
    # max_cnt > k하면  
    if cnt[max_val] > k:
        #<= k까지 s를 증가시킨다
        while cnt[max_val] <= k:
            cnt[data[s]] -= 1
            s += 1
            
