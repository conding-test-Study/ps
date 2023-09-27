# 답 찾아봄
# 숫자 길이기 세 자리 이상일때 분할을 어떻게 할지 떠올리는게 관건
# 이중 반복문을 통해 숫자를 세구간으로 분할
# 분할 후 재귀를 활용

import sys
input = sys.stdin.readline

min_n = float('inf')
max_n = 0
def count(n):
    n = str(n)
    cnt = 0
    for a in n:
        if int(a) % 2 != 0:
           cnt += 1
    return cnt

def divide(n, cnt):
    global min_n, max_n
    s = str(n)
    cnt += count(s)

    if len(s) == 1:
        min_n = min(min_n, cnt)
        max_n = max(max_n, cnt)
        return
    elif len(s) == 2:
        divide(int(s[0]) + int(s[1]), cnt)
    else:
        for i in range(1, len(s)-1):
            for j in range(i+1, len(s)):
                # 숫자를 세 구간으로 나누는 테크닉
                a = s[:i]
                b = s[i:j]
                c = s[j:]
                new_n = int(a) + int(b) + int(c)
                divide(new_n, cnt)
n = int(input())
divide(n, 0)
print(min_n, max_n)


