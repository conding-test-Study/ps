# 시간 초과 답지 확인
n, x = map(int,input().split())
num_visit = list(map(int, input().split()))
cnt = 0
max_sum = -1

# 과정 끝나기전 0이면 그냥 끝내기 
if max(num_visit) == 0:
    print("SAD")
else:
    sum_visit = sum(num_visit[0:x])  #초기값 설정하고 cnt = 1 max_sum 초기화 생각 못함
    max_sum = sum_visit
    cnt = 1

    #s, e대신 0:x로 하니까 변수 줄어서 간단해보이기도 하고 s,e가 이해 도움될 수도 있고
    #슬라이딩 윈도우  구간의 모든 합을 계산하는 것이 아닌 하나 빼고 하나 더한다.     
    for i in range(x, n):
        sum_visit += num_visit[i]
        sum_visit -= num_visit[i-x]
        if sum_visit > max_sum:
            max_sum = sum_visit
            cnt = 1
        elif sum_visit == max_sum:
            cnt += 1    
    
    print(max_sum)
    print(cnt)

