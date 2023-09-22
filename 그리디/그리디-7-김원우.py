# 정답참고함

import sys

input = sys.stdin.readline
n, space = map(int, input().split())
m = int(input())
box = [0] * (n + 1)
send = []
answer = 0

for i in range(m):
    a, b, amount = map(int, input().split())
    send.append([a, b, amount])
send.sort(key=lambda x: (x[1], x[0]))

for start, destination, boxes in send:
    maxbox = boxes

    for i in range(start, destination):
        # 주어진 박스 수 vs 해당 마을에서 실을 수 있는 최대 박스 수
        # 둘 중 최솟값을 적용
        maxbox = min(maxbox, space - box[i])

    for i in range(start, destination):
        # 적용한 최솟값은 다시 box배열에 반여해서 해당 마을에서 실을 수 있는 최대 박스 수 갱신
        box[i] += maxbox

    answer += maxbox
print(answer)

# box배열을 통해 출발 마을부터 도착지 마을까지 얼마나 싣고 가야할지 체크하는게 관건
# 그리디인데 왠지 DP냄새가 살짝나는듯한 굉장히 어려운 문제같다..
# 실전 코테에서 만났으면 절대 못풀었을듯;