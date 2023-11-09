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
