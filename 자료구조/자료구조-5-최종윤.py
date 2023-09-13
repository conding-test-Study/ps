가장 어려운것이 여러개면 문제 번호가 큰 것을 출력한다는 점에서 우선순위 큐가 떠올라 heapq를 사용해서 풀수있지 않을까 했다.

가장 쉬운것이 여러개면 문제번호 큰것을 출력하는 명령어도 있기 때문에 하나의 힙큐에서 가능한지 생각해봤지만, 
가장 쉬운거 가장 어려운거 동시에 뽑아내는 heapq는 불가능하다. 최대힙 최소힙 둘 중 하나인듯
L, -L, P 넣어도 결국 첫번째 우선순위로 둘중 하나를 먼저 뽑아내는 것만 가능하다.
쉬운거를 L,P로 어려운거를 -L, -P로 넣는거를 생각했다.

  
1. 문제번호 P를 제거하는 solved P 명령어가 있었는데 heapq에서는 가장 작은거 큰거만 제거하지 특정 값을 제거하면 힙 자료구조가 무너지지 않을까 생각했다.
P를 바로 제거해버리면 heappop했을 때 이상해질듯 맞춰서 정렬해놓은건데 앞으로 떙겨지니까.
P 제거된 표시만 in_list에 False로 해두고 P가 heap의 가장 앞에 위치할때만 뽑아 heappop으로 제거하면 가능하다.
  
2. heapq에서 P값 갖는걸 제거하고 여러번 제거해서 큰 것들이 없어지면
recommend 해서 가장 큰걸 조회할 때 루트에 있던게 없어진건데 할 heappop가능? 
P 제거된 표시만 in_list에 False로 해두고 P가 heap의 가장 앞에 위치할때만 뽑아 heappop으로 제거하면 가능하다.



3. recommend 에서 없애는게 아니라 조회만하는데? heapq에서 넣는거 뺴는거밖에 안 배웠는데    
그냥 배열[0]번쨰꺼 조회하면 되나?그렇다

4.  답지보니 다 defaultdict라는 걸 쓰던데 뭔지 왜 쓴건지 봐야겠다. 
k,v을 저장하는 dict인데 저장 안된 키의 값을 자료형 기본 값으로 초기화해서 조회한다.
키의 개수를 세야할 때, 리스트나 셋의 항목을 정리해야할 때 사용한다.
defaultdict를 사용하지 않으면 키의 개수를 셀때  키 값이 존재하는지 확인하고 0으로 초기화하는 코드가 추가되야한다.
https://dongdongfather.tistory.com/69

스택 큐를 써서 하는것도 생각해봤지만 그 안에서 정렬을 해야하는 방법밖에 떠올리지못해 시간초과 발생할것 같았다.

  답지 풀이 
import sys
input = sys.stdin.readline
from heapq import heappop,heappush
from collections import defaultdict


N = int(input())
min_heap = []
max_heap = []
in_list = defaultdict(bool)
for _ in range(N):
    P, L = map(int, input().split())
    heappush(min_heap,[L,P])
    heappush(max_heap,[-L,-P])
    in_list[P] = True

M = int(input())
for _  in range(M):
    command = input().split()
    if command[0]=='recommend':
        if command[1]=='1':
            while not in_list[-max_heap[0][1]]:
                heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while not in_list[min_heap[0][1]]:
                heappop(min_heap)
            print(min_heap[0][1])
    elif command[0]=='solved':
        in_list[int(command[1])] = False
    else:
        P = int(command[1])
        L = int(command[2])
        # 같은 번호의 다른 난이도 문제가 삽입되어 이미 죽은 문제인데 True로 나와 출력되는 것을 방지.
        while not in_list[-max_heap[0][1]]:
            heappop(max_heap)
        while not in_list[min_heap[0][1]]:
            heappop(min_heap)
        in_list[P] = True
        heappush(max_heap,[-L,-P])
        heappush(min_heap,[L,P])
