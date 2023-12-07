#s.count(target)하면 그냥 풀리더라 문자만 세는 것이아닌 문자열을 세준다.
#첫글자가 같은게 나오면 거기서부터 비교하기도 하더라
#len(split(target))하면 target 수 +1 만큼 이니까 -1해서 구하기도 하더라

T = 10
for tc in range(1, T + 1):
    t = input()
    target = input()
    s = input()
    
    start = 0
    end = len(target)
    cnt = 0
    while end < len(s) + 1:
        if s[start:end] == (target):
            cnt += 1
        start += 1
        end += 1
    print("#{} {}".format(tc, cnt))
