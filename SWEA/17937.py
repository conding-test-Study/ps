import math
 
T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    
    for i in range(a, b + 1):
        if (a == 1):
            break
        a = math.gcd(a, i)
 
    print("#{0} {1}".format(tc, a))
