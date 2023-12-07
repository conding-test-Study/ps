#답지 확인
에라토스테네스의 체 : 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법. 
합성수를 지운다더니 배수가 합성수인가? 
2의 배수 안 지운 것중 가장 작은 3을 소수에 넣고 3의 배수 지우기
안지운것중 작은 5의 배수 모두 지워나가네 
1. 에라토스테네스의 체 : 주어진 N까지의 소수를 미리 구한다. ( 모든 경우를 체크해서 소수를 만들 경우 시간 초과가 발생합니다. )

2. 투포인터 : start, end 두 개의 포인터를 이용해서 원하는 값보다 작은 경우 end += 1을 큰 경우에는 start += 1을 적용해서 end가 N이 될때까지 수행합니다.

풀이 코드

import math

N = int(input())

a = [False, False] + [True] * (N-1)
prime_num = []

for i in range(2, N+1):
    if a[i]:
        prime_num.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

answer = 0
start = 0
end = 0
while end <= len(prime_num):
    temp_sum = sum(prime_num[start:end])
    if temp_sum == N:
        answer += 1
        end += 1
    elif temp_sum < N:
        end += 1
    else:
        start += 1

print(answer)
