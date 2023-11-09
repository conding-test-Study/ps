#답지 확인
        #2초에 store 알려면? t증가시키면서 m되면 store += k
    #m때 여러 개 저장해놓았다가 a[i+1]에게 준다. -1    -> 시간초과
        #반복문을 중첩하진 않았지만 이건 t 1만 인데 계산식은 n 100에 대해서만 연산하면 되긴 해보임

 #계산식을 만들어서 할 수도 있겠따 생각했지만- 아니  적어놓지도 않음..
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrivedAt = list(map(int, input().split()))
    arrivedAt.sort()
    store = 0
    t = 0
    i = 0
    answer = "Possible"

    while i < n:
        store = (arrivedAt[i] // M) * K - (i + 1)
        if store < 0:
            answer = "Impossible"
            break   
        i += 1

    print("#{} {}".format(tc, answer))

#처음풀이  
 while i < n:
        if t != 0 and t % m == 0:
            store += k
        if t == arrivedAt[i]:
            if store > 0:
                store -= 1
                i += 1
            else:
                answer = "Impossible"
                break   
        t += 1



    print("#{} {}".format(tc, answer))
    
