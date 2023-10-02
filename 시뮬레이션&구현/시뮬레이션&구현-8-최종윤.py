def solution(numbers, hand):
    answer = ''
    r = 12
    l = 10
    
    for num in numbers:
        if num in [1,4,7]:
            answer += ('L')
            l = num
        elif num in [3,6,9]:
            answer += ('R')
            r = num
        else:
            #l과 r의 num까지의 거리 같으면 hand로 - l위치, r위치 - 이전 num값
            l_p = ((l-1)//3, (l-1) % 3)
            r_p = ((r-1)//3, (r-1) % 3)
            if num == 0:
                num = 11
            n_p = ((num-1)//3, (num-1) % 3)
            print("lp: ",  l_p, "r_p: ", r_p)
            l_d = abs(n_p[0] - l_p[0]) + n_p[1] - l_p[1] 
            r_d = abs(n_p[0] - r_p[0]) + r_p[1] - n_p[1]
            print("ld: ",  l_d, "r_d: ", r_d)
            
            if r_d < l_d:
                r = num
                answer += ('R')
            elif l_d < r_d:
                answer += ('L')
                l = num
            else:
                if hand == "right":
                    r = num
                    answer += ('R')
                else:
                    answer += ('L')
                    l = num
    return answer
