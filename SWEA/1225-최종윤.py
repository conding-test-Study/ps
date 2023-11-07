from collections import deque
T = 10
for tc in range(1, T+1):
    t = int(input())
    data = list(map(int, input().split()))
    q = deque(data)
    x = 1
    while True:
        if x > 5:
            x = 1
        val = q.popleft()
        if val - x <= 0:
            q.append(0)
            break
        q.append(val - x)
        x += 1


    print("#{}".format(tc), end = ' ')
    for n in q:
        print(n, end = ' ')
    print()
