#답지 확인
# 어려워진건지 공부가 하기 싫은 시기인건지 잘 안들어가서 그냥 
#답지라도 보면서 이해해보고자 했음

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


#투 포인터를 쓴다는데 투포인터는 인덱스 2개를 가리키는 변수를 만들고 리스트를 순차적으로 접근하여 처리하는 알고리즘
# 슬라이딩 윈도우도 리스트를 순차적으로 접근하여 구간 합을 구하는데 구간 길이가 일정하다는 특징이 있다.

#대표예제로 첫인덱스 끝 인덱스로 사용하여 
#인덱스 사이에 있는 리스트의 부분 합이 특정 값M이 되는 경우를 찾는데 사용한다.

#리스트에서 두개 값 합이 초과 넘지 않는 걸 찾는다는 점에서 투포인터? 
#가장 작은거 큰거 끼리 더해야했으니 정렬? 
# 전체 크기에서 구명보트 개수를 빼면서 보트 1개를 1로 취급하고 
  #짝 안 지어진 사람들 1보트로 취급하여  답 구함


#이게 이해가 더 쉽고 풀어낸다면 이렇게 푸는 방법을 생각하기 좋을것같다. 과정그대로 구현해낸거니까..
#정렬을 한다음 큰거 작은거 같이 합을 보면 된다는걸 생각못했다. 왜 두개 짝 만들어서 최소할때 큰거 작은거 고르면 된다는 생각은 했던것같은데?
#큰거 작은거 뽑으려면 정렬 생각해써야지 하나씩 구현했어야지 한꺼번에 하려고하지말고..

people 리스트를 덱으로 만든 후 내림차순 정렬

무거운 사람(왼쪽)과 가벼운 사람(오른쪽)을 인덱스로 매칭

합이 보트 무게보다 가벼우면 둘 빼냄

보트 무게보다 무거우면 무거운 사람만 빼냄

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit: # 최댓값과 최솟값 묶어서 보트태움
            answer += 1
            people.pop()    #최소 빼내고
            people.popleft()    #최대 빼내고
        else:
            answer += 1
            people.popleft()
            
    if people:  #people에 1명 남아있는 경우 처리
        answer += 1
                
    return answer
