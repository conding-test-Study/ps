# 슬라이딩 윈도우로 풀음

import sys
input = sys.stdin.readline

n, x = map(int,input().split())
arr = list(map(int,input().split()))

answer = []
start = 0
end = x-1
summation = sum(arr[start:end+1])
answer.append(summation)

while True:
    if end == len(arr)-1:
        break
    tmp = summation - arr[start] + arr[end+1]

    if tmp >= summation:
        answer.append(tmp)
    summation = tmp
    start += 1
    end += 1

if summation == 0:
    print("SAD")
else:
    a = max(answer)
    print(a)
    print(answer.count(a))
