from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        for c in skill_trees[i]:
            if c not in skill:
                skill_trees[i] = skill_trees[i].replace(c, '')
                
    q = deque()
    n = len(skill)
    q.append([skill[0], 0])
    q.append(["", 0])
    
    comb = [""]
    temp = ""
    for c in skill:
        temp += c
        comb.append(temp)
        
    
    print("trees: ", skill_trees)
    print("comb: ", comb)
    for tree in skill_trees:
        if tree in comb:
            answer += 1
    #skill에 들어있는 게 아닌거는 다 뺴고 skill 문자를 bfs로 모든 경우의수 중에 해당되는 경우라면 +1
    return answer


# dfs인줄알고 그에 맞춰서 생각하다가 문제 잘못이해하고 푼 풀이 

from collections import deque

def solution(skill, skill_trees):
    answer = 0


    #타겟넘버에서 배열에 들어있는거 더하든지 뺴든지 두가지 경우로 그래프로 쳐서 탐색하는것처럼
    
    for i in range(len(skill_trees)):
        for c in skill_trees[i]:
            if c not in skill:
                skill_trees[i] = skill_trees[i].replace(c, '')
                
    q = deque()
    n = len(skill)
    q.append([skill[0], 0])
    q.append(["", 0])
    
    comb = []
    while q:
        temp, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([temp + skill[idx], idx])
            q.append([temp, idx])
        else:
            comb.append(temp)
    print("trees: ", skill_trees)
    print("comb: ", comb)
    for tree in skill_trees:
        if tree in comb:
            answer += 1
    #skill에 들어있는 게 아닌거는 다 뺴고 skill 문자를 bfs로 모든 경우의수 중에 해당되는 경우라면 +1
    return answer
