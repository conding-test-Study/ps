#답지 확인
#한 변수에 대해 1부터 전체범위까지 완전탐색하고  나머지 변수가 조건에 맞는지 확인 생각못함

def solution(brown, yellow):
    total = brown + yellow 
    for y in range(3, total + 1):
        if (total / y) % 1 == 0:
            x = total // y
            if x >= y:
                if 2 * x + 2 * y == brown + 4:
                    if (y-2)*(x-2) == yellow:
                        return [x, y]
    
