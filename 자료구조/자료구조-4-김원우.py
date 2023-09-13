import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
q = PriorityQueue()
for i in range(n):
    num = int(input())
    tmp = [abs(num), num] # 절댓값이랑 원래값 같이 저장

    if num == 0:
        if q.empty():
            print(0)
        else:
            print(q.get()[1])
    else:
        q.put(tmp)

