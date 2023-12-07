#테케가 하나라 까먹고 띄어쓰기 안 해서 틀림
t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = [0] * 5001
    for _ in range(n) :
        a, b = map(int, input().split())
        for i in range(a, b + 1) :
            data[i] += 1

    result = []
    p = int(input())
    for _ in range(p) :
        c = int(input())
        result.append(data[c])

    print(f'#{tc}', *result)
