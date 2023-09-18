#전에 풀었던 문제라서 갑자기 뒤 값만 작은거를 계속 고르면 되는게 떠오름 
# x[1] 같은 것에 대해 x[0] 오름차순으로 정렬하는거 뺴먹음
import sys
input =  sys.stdin.readline
n = int(input())

c = []
for i in range(n):
    c.append(list(map(int,input().split())))

c.sort(key = lambda x: (x[1], x[0]))

ans = 0
e = 0

for i in range(n):
    if e <= c[i][0]:
        e = c[i][1]
        ans += 1
print(ans)
