# 코드 참고 출처: https://myjamong.tistory.com/317
# 누적변수 카운트 + 캐시 리스트에서 l2의 인덱스별로 누적변수 저장하기

import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))
