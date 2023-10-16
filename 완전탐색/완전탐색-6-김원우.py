# 완탐+그리디같은 느낌?
def solution(sizes):
    answer = 0
    
    hMax = 0
    wMax = 0
    
    for i in range(len(sizes)):
        h = sizes[i][0]
        w = sizes[i][1]
        
        if h < w:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        
        wMax = max(wMax, sizes[i][0])
        hMax = max(hMax, sizes[i][1])
    
    
    answer = wMax * hMax
    return answer
