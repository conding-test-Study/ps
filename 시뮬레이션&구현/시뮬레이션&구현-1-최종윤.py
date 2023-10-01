#답지 보고 풀었음 조건들을 조건문으로 해보려고했음 정렬하면 쉽게 할 수 있었음 
#주위 인접 좋아하는 사람 많은 것부터 같은것 들에 대해 빈칸 많은것부터 같은 문구에서 정렬을 떠올리지 못함 
#방문안한곳에대해서 범위 안 벗어나도록 

import sys
input = sys.stdin.readline

n = int(input())

arr = [[0] * n for _ in range(n)]

students = []
for i in range(n**2):
    students.append(list(map(int,input().split())))



# U,D,L,R
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

###1 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.

# 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다. 1~n^2
for student in students:
#좋아하는 학생위치 담을 loc1
    
    tmp = []
    # 2차원 배열에서 student[1] ~ stud[4]까지 모두 탐색한다. 4 n^2   n이 20이라 ㄱㅊ
    for j in range(n):
        for k in range(n):
            if arr[j][k] == 0:
                like = 0
                blank = 0
                for i in range(4):
                    nr, nc = j + dr[i], k + dc[i]
                    if 0 <= nr < n and 0 <= nc < n:
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1

                tmp.append([like,blank,j,k])
  ### !!!! like, blank는 클 수록, 행과 열의 수는 작을수록 답이니 lambda 뒤의 조건을 잘 줘야함!!!
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    arr[tmp[0][2]][tmp[0][3]] = student[0]
students.sort()                    
result = 0
for i in range(n):
    for j in range(n):
        like = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    like += 1
        if like != 0:
            result += 10 **(like-1)
print(result)
