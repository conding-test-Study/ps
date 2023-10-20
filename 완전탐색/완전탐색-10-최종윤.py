#답지확인
#combination도 permutation도 같은 것을 여러개 선택해서 조합해주지는 않는다.
#그렇다면 혹시 반복문?이 떠올랐는데 가능할까? 중복순열?이라고 해야하나?
#아 글자 순서 착각했다..... A E IO U순서로 한글자 두글자 이렇게 커지는줄  반복문도 확실히 안 되는듯

#A -> E - I O U순서로 방문하는 DFS같은데 다시 보니까? 결국 dfs구현만 할 수 있을면 될듯?
#그러니까 arr를 순서대로 계속 방문하면 될듯 길이 5될때까지
#방문배열은 어떻게 해야할까? 없어야 계속 방문하니 없고 종료조건은 확실히 필요한듯 return문도
#범위 벗어나는거 방문 안하는거 고려 안해도 되고 연결노드는 그냥 arr 반복문 돌리면 되고 

def solution(word):
    ans = []
    arr = 'AEIOU'
    def dfs(w, cnt):
        if cnt == 5:
            return
        for c in arr:
            ans.append(w + c)
            dfs(w + c, cnt + 1)
    #정해진 순서대로 ans 배열에 문자들이 쌓이겠지
    dfs('', 0)
               
    return ans.index(word)+1


#틀린 풀이 
import sys
sys.setrecursionlimit(10**6)

arr = ['A', 'E', 'I', 'O', 'U']
def dfs(result):
    if len(result) == 5:
        return result
    for c in arr:
        result += c
        dfs(result)
#recursion수가 너무 많다고하는데 .. 5^5        10^3까지니까 그런가? 다 구한다음 하는게 아니라
#cnt세다가 나오면 그떄 return해야하나
def solution(word):
    
    ans = []
    #정해진 순서대로 ans 배열에 문자들이 쌓이겠지
    ans.append(dfs(''))
               
    return ans.find(word)
