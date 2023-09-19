# 답 찾아봄

import sys
input = sys.stdin.readline

periods = []
answer = 0
n = int(input())

for _ in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    periods.append((m1*100+d1, m2*100+d2))

periods.sort(key=lambda x:(x[0], x[1]))
wither_date = 301 # 꽃이 지는 날 저장
end = 0
while periods:
    # 꽃이 지는 날이 12월 1일을 넘거나 그 날에 더이상 필 꽃이 없는 경우
    if wither_date >= 1201 or wither_date < periods[0][0]:
        break

    for period in periods[:]:
        # 시작일 <= date <= 지는 날인 경우
        if wither_date >= period[0]:
            if end <= period[1]: # 이전의 저장한 꽃의 지는 날보다 현재 꽃의 지는 날이 더 뒤에 있는가?
                end = period[1] # 꽃이 지는 날 저장
            periods.remove(period) # 배열에서 제거
        else:
            break

    answer += 1
    wither_date = end

print(0 if wither_date < 1201 else answer)