T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    b = bin(M)[2:]
    if b[len(b) - N:].count('1') == N:
        answer = "ON"
    else:
        answer = "OFF"


 
    print("#{} {}".format(tc, answer))

