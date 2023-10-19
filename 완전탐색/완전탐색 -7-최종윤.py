# 답지 확인
# permutations 생각 못함 dfs로 풀수 있지 않을까 가능한 모든 경우의수를 순서 바꿔가면서 탐색하니까

from itertools import permutations

def solution(numbers):
    cnt = 0
    permut = []
    for n in range(1, len(numbers) + 1):
        for x in permutations(numbers, n):
            permut.append(int(''.join(x)))
    permut = set(permut)
            
            
    for x in permut:
        if x < 2:
            continue
        isPrime = True
            #x==2면 소수
        for i in range(2, int(x ** 0.5)+1):
                # 2~ root x 까지 나누어 떨어지는 수가 있는 경우 소수X
            if x % i == 0:
                isPrime = False
                break
                #loop 끝까지 없다면 소수ㅇ
            
        if isPrime:
            print(x)
            cnt += 1
    return cnt
