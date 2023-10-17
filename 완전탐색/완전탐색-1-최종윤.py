#답지 확인
#문제 그리디 가능한지 예시 확인 안 해보고 그리디로 구현하기 시작했음
#그리디X - 35-1개,40-1개 보다 40-2개가 최소값이기 때문
#완전탐색을하는데 비트마스크 또는 DFS 백트래킹으로 풀 수 있다.


# dfs로 구현


import sys
from collections import defaultdict

count  = defaultdict(int)
select_cnt = defaultdict(int)


T = input()
len = len(T)
for c in T:
    count[c] += 1

n = int(input())

books = []
for i in range(n):
    books.append(list(input().split()))

min_val = sys.maxsize

def check():
    for key in count:
        if count[key] > select_cnt[key]:
            return False
    return True


def dfs(idx, total):
    global min_val
    if idx == n:
        if check():
            min_val = min(min_val, total)
        return

    for c in books[idx][1]:
        select_cnt[c] += 1
    dfs(idx + 1, total + int(books[idx][0]))
    for c in books[idx][1]:
        select_cnt[c] -= 1
    dfs(idx + 1, total)



dfs(0,0)
if min_val == sys.maxsize:
    print(-1)
else:
    print(min_val)



###############################################################
#비트마스킹
import sys


in_str = input()
bcnt = int(input())
price = []
in_major = []
for i in range(bcnt):
    p, m = input().split()
    price.append(int(p))
    in_major.append(m)
def wordinbook(word, book, price):
    cnt = 0
    for w in word:
        if w in book:
            cnt += 1
            book = book.replace(w, ' ', 1) # 오려낸 글자는 없애준다
            # print(book, word)
            if cnt == len(word):
                return price
    return sys.maxsize

result = []

for i in range(1 << len(in_major)):
    search_str = ""
    sum_price = 0
    for j in range(len(in_major)):
        if (i & 1 << j) != 0: # 
            search_str += in_major[j]
            sum_price += price[j]

    result.append(wordinbook(in_str, search_str, sum_price))

result = min(result)
if result == sys.maxsize:
    result = -1

print(result)

