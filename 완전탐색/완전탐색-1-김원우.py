# 반례 아직 해결못함.
import sys
input = sys.stdin.readline

targetStr = input().strip()
n = int(input())
books = [list(map(str,input().strip().split())) for _ in range(n)]
ans = sys.maxsize
visited = [0] * len(targetStr)
books.sort()
buy = set()

def dfs(curlen, price, buy):
    global ans
    if curlen == len(targetStr):
        ans = min(ans, price)
        return
    if price > ans:
        return

    for k in range(len(books)):
        name = books[k][1]
        if targetStr[curlen] in name:
            idx = name.index(targetStr[curlen])
            curPrice = int(books[k][0])
            tmpCh = name[idx]
            ## 이 부분 수정필요
            books[k][1].replace(tmpCh, ' ') # 같은 알파벳있으면 중복되는 문제 발생, 해결필요함
            print(books[k][1], tmpCh)
            ##

            check = False
            if k in buy:
                curPrice = 0
                check = True
            buy.add(k)

            dfs(curlen+1, price+curPrice, buy)
            books[k][1].replace(' ', tmpCh)
            if not check:
                buy.remove(k)

dfs(0,0,buy)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)