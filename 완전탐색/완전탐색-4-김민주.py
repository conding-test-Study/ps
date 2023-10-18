import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

print(nums)

nums.sort()
cnt_1 = N

for i in range(N-1):
    if nums[i] + nums[i+1] <= nums[-1]:
        cnt_1 -= 1

    if nums[i] + nums[i+1] > nums[-1]:
        break

cnt_2 = N

for j in range(N):
    print("현재 좌표: ", j)
    if nums[0] + nums[1] <= nums[N-1-j]:
        cnt_2 -= 1
    if nums[0] + nums[1] > nums[N-1-j]:
        break

print(cnt_1)
print(cnt_2)

print(max(cnt_1, cnt_2))


# 원소 3개 컨트롤하여 범위를 알아내는 게 중요함
n = int(input())
data = sorted(list(map(int, input().split())))
if n > 2:
    result = 2
    for start in range(n-2):
        end = start+2
        while True:
            if data[start] + data[start+1] > data[end]:
                result = max(result, end-start+1)
                end += 1
                if end == n:
                    break
            else:
                break
    print(result)
else:
    print(n)
