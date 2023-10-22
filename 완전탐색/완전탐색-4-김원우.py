# 약간 투포인터느낌

import sys
input = sys.stdin.readline


n=int(input())

nums=list(map(int,input().split()))
nums.sort()

answer=1

for x in range(n - 1):
    for z in range(n - 1, -1, -1):
        if z<x+1:
            break
        if nums[x]+nums[x+1]>nums[z]:
            answer=max(z-x+1,answer)

print(answer)