def findSmallestX(case) :
    a, b, c = case
    changes = []
    # a를 변경할 경우
    diff = c - b
    x = abs(b - diff - a)
    changes.append(x)
    # b를 변경할 경우
    mid = (a + c) / 2
    x = abs(mid - b)
    changes.append(x)
    # c를 변경할 경우
    diff = b - a
    x = abs(b + diff - c)
    changes.append(x)
 
    return min(changes)
 
 
testcaseNumber = int(input())
for i in range(testcaseNumber) :
    case = list(map(int, input().split()))
    answer = findSmallestX(case)
    print("#%d %0.1f" % (i + 1, answer))
