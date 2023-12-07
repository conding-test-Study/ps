#답지확인

import sys
read = sys.stdin.readline

word1, word2 = input(), input()
w= len(word1)
h= len(word2)
cache = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if word1[i-1] == word2[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])
print(cache[-1][-1])
#w,h를 바꿔서 하니까 indexError가 발생한
#반례
#첫번째 문자열과 두번째 문자열의 순서에 따라 정답과 오답이 바뀌는 문제입니다.
#오답:8
#정답:3
qsdferrfgtfsawfsefeesgdtdrgthyytfgfddsdawdwd
efvs
