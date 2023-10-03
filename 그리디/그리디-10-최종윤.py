def solution(n, lost, reserve):
#lost랑 reserve둘다 지웠다가 for _ in lost 에서 lost.remove하니까 제대로 안 됨 

    set_reserve = (set(reserve)-set(lost))
    set_lost = set(lost) - set(reserve)
    for r in set_reserve: 
        if (r-1) in set_lost:
            set_lost.remove(r-1)
        elif (r+1) in set_lost:
            set_lost.remove(r+1)
            
    return n - len(set_lost)
