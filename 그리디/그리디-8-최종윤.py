#문자열에서 삭제를한다길래 떠오른게 replace 하나 있었는데 흠.. 복잡한거 싫어...

#답지 확인함..  제거하기? 문자열에서 큰수 만들기?.. 유형외우기라도 해야지..

#구글링하는데 조합정렬했다가 실패하더라 나는 조합도 모른다..
#list(combinations(list(number), len(number)-k))                  
#n개 리스트를 주고,, 수만 주면 모르니까    ,   nCr이니까 n과 r이 파라미터로 있겠지
#조합같은거를 종종 보게 되는듯   반복문해서 인덱스를 i+1 j+1이런식으로  nC3  nC2이런건 해본거 같다
#두번 쨰로 뽑는거를 크게하도록 해서 순서 바뀌지 않도록 하더라
https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
#i

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])
