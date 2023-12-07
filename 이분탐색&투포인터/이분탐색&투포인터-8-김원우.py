n, m = map(int,sys.stdin.readline().split())
house = []
for i in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()
start = 1
end = house[-1] - house[0]
ans =0

while start <= end:
    mid = (start+end)//2
    current = house[0]
    cnt = 1

    for i in range(1,n):
        if house[i] >= current+mid:
            cnt += 1
            current = house[i]
    if cnt >= m:
        start = mid+1
        ans = mid
    else:
        end = mid-1

print(ans)
