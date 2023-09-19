#답지확인
# 꽃이 피고 지는 날짜에 대해 월에 100을 곱한 뒤, 일이랑 덧셈 하는 것을 생각하지 못함
# ->  100곱해서 하니 해당날짜 이상 이하 조건문 쓸 때 조건문이 간단해지는 것 같다.


#end = [ (3,1), (6,30), (12,10) ]
#tmp(heap end ) = [(6,30)x  (12,10)x (8,31), (5,31)] 

#tmp에 flower지는 날짜 계속 넣어서  
#end[-1]보다 flower시작 날짜가 커지면 
#tmp에서 가장 큰 flower 지는 날짜 end에 넣는다.

#비슷한문제에서 힙큐 써서 큰거 뽑는거니까 혹시해서 써봤다.
#날짜가 이상인지 이하인지 처리하다가 같은 월 다른월 따로 처리하기가 귀찮았다.
#마지막 12.10이 안 들어가길래 end[-1]을 flower시작점이 안 넘어가고 끝난 경우
# 11.30지났는지 확인하고 가장 큰 걸 넣어줘야한다고 생각했다.


#첫 풀이
import sys
import heapq

input = sys.stdin.readline

n = int(input())

flowers = []
for i in range(n):
    flowers.append(list(map(int,input().split())))

end = [(3, 1)]
tmp = []
for i in range(n):
    # 시작점 기준점을 넘어가면  가장 늦게 지는걸 넣는다 end에
    if flowers[i][0] > end[-1][0] and flowers[i][1] > end[-1][1]:
        m, d = heapq.heappop(tmp)
        end.append((-m, -d))


    #현재보는거 시작점이 기준점 안 넘어가면 tmp에 가장 늦게지는걸 찾기위해 넣는다.
    if flowers[i][0] <= end[-1][0] and flowers[i][1] <= end[-1][1]:
        heapq.heappush(tmp, (-flowers[i][2], -flowers[i][3]))
    elif flowers[i][0] < end[-1][0]:
        heapq.heappush(tmp, (-flowers[i][2], -flowers[i][3]))

    #기준점 안 넘어가고 끝난 경우
#마지막 선택 지는게 11,30 미만일 경우
if (end[-1][0] == 11 and end[-1][1] < 30) or end[-1][0] < 11:
    m, d = heapq.heappop(tmp)
    end.append((-m, -d))
    if end[-1][0]




#end = [ (3,1), (6,30), (12,10) ]
#tmp(heap end ) = [(6,30)x  (12,10)x (8,31), (5,31)] 


  
###########답지

import sys

# 꽃들의 총 개수 N
n = int(sys.stdin.readline())

# 꽃들이 피고 지는 날짜
arr = []
for _ in range(n):
    # 꽃이 피고 지는 날짜에 대해 월에 100을 곱한 뒤, 일이랑 덧셈
    start_m, start_d, end_m, end_d = map(int, sys.stdin.readline().split())
    arr.append([start_m * 100 + start_d, end_m * 100 + end_d])

# 꽃이 피는 날짜, 꽃이 지는 날짜순으로 오름차순 정렬
arr.sort()

# 정원의 마지막 꽃이 지는 날짜
end_date = 301

# 심은 꽃의 개수
count = 0

# 더 이상 확인할 꽃이 없을때까지
while (arr):

    # 정원의 마지막 꽃이 지는 날짜가 12월 1일 이상이 됐거나,
    # 현재 확인할 꽃의 시작 날짜가 정원의 마지막 꽃이 지는 날짜와 이어지지 않을 경우, 탐색 종료
    if (end_date >= 1201 or arr[0][0] > end_date):
        break

    # 꽃이 피는 날짜가 end_date 이전일 때, 가장 느리게 지는 꽃의 날짜
    temp_end_date = -1

    for _ in range(len(arr)):

        # 꽃이 피는 날짜가 end_date 이전이라면,
        if (arr[0][0] <= end_date):
            # 그 중 가장 느리게 지는 꽃의 날짜를 확인
            if (temp_end_date <= arr[0][1]):
                temp_end_date = arr[0][1]

            # 확인한 꽃은 원본 배열에서 제거
            arr.remove(arr[0])

        else:
            break

    # 가장 꽃이 느리게 지는 날짜를 end_date로 수정
    end_date = temp_end_date
    # 심은 꽃의 개수 증가
    count += 1

# 마지막으로 확인한 꽃의 지는 날짜가 12월 1일 보다 작으면, 
# 3월 1일부터 11월 30일까지 계속 피어있는게 아니므로 0 출력
if end_date < 1201:
    print(0)
else:
    print(count)
