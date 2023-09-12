import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for i in range(T):
    command = [s for s in input()] # 명령어
    command.pop() # 개행 제거

    n = int(input())
    num = eval(input())
    arr = deque(num)

    flag = 0
    reverseCnt = 0 # 뒤집기 갯수 세는 용도
    for c in command:
        if c == 'R':
            reverseCnt += 1
        elif c == 'D':
            if len(arr) == 0:
                print("error")
                flag = 1
                break
            else:
                if reverseCnt % 2 == 0:
                    # 뒤집기 횟수가 짝수일때
                    arr.popleft()
                else:
                    # 뒤집기 횟수가 홀수일떄
                    arr.pop()
    if flag == 0:
        if reverseCnt % 2 == 0:
            print("[" + ",".join(map(str, arr)) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(map(str, arr)) + "]")
