# 비교적 간단한 백트래킹

def solution(word):
    answer = -1
    cnt = -1
    dic = ['A', 'E', 'I', 'O', 'U']
    flag = 0

    def dfs(s):
        nonlocal word, answer, cnt, flag
        cnt += 1
        print(''.join(s), answer)
        if ''.join(s) == word:
            answer = cnt
            flag = 1
            return
        if len(s) == 5:
            return

        for a in dic:
            s.append(a)
            dfs(s)
            s.pop()
            if flag == 1:
                return

    dfs([])

    return answer