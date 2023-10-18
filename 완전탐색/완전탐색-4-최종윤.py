# 답지확인

#문법은 아는 거긴 한데 저렇게 앞에서 2개를 가지고 큰것만 하나씩 증가시키면서 성립한다는 관계를
#파악한다는 생각을 못한다. 뭐 수학적 사고 같은건가?


n = int(input())
# 작은 것 2개를 선택하여 크기 비교를 그 다음 작은 것 부터 해보기 위해 정렬?
# 예시를 보고 관계 파악?  3,4,5 있으면 3+4>5 만족되면 3+5>4, 4+5>3 은 자연히 만족된다는 걸 알 수 있다?
#왜냐하면 작은 것 두개가 x,y 일때  x+y>z 이면 나머지 두개도 성립한다는 걸 아니까?


data = sorted(list(map(int,input().split())))

if n>2:
    result = 2
    for start in range(n-2):
        end = start+2
        while True:
            #큰수만 계속 증가시키며 더 긴 삼각수열 찾고  만족 안 하면 이후 수는 비교 필요가 없다
               #3,3,4,5,6,7있으면 3+3>4,5 까지 만족하고 3+3>6 만족x 그 뒤에있는 7은 당연히 만족x
             #이후 3+4>5 3+4>6 이렇게 비교한다?  이는 idx 0과 2가 선택된 것이 아닌 idx 1과2로 start를 앞 한칸 옮긴것 
            #가장 긴 삼각 수열이므로 

            if data[start] + data[start+1] > data[end]:
                result = max(result, end - start + 1)
                end += 1
                if end == n:
                    break
            else:
                break
    print(result)
else:
    #길이 2 이하이면 항상 삼각수열 인 것을 예제 입력대로 출력하도록 하면 알 수 있다.
    print(n)
