# 반례 해결 완료
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
            tmpList = list(name)
            tmpList[idx] = '-'
            books[k][1] = ''.join(tmpList)

            check = False
            if k in buy:
                curPrice = 0
                check = True
            buy.add(k)

            dfs(curlen+1, price+curPrice, buy)
            tmpList = list(books[k][1])
            tmpList[idx] = tmpCh
            books[k][1] = ''.join(tmpList)

            if not check:
                buy.remove(k)

dfs(0,0,buy)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)