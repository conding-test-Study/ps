# 답지 확인

# 문자열에서 최소값 찾기 위해 리스트로 변환하는거 생각못함 
# 싫어도 참고 하나씩 적어보기 

# 최소값 찾고 인덱스 찾고 
#인덱스 오른쪽에서 다시 최소값 없을 때까지 찾고 
#그다음 인덱스 왼쪽에서 최소값 찾는걸 생각 못함 

#이걸 첨부터 아는게 아니라 이것저것 시도 해보다가 규칙을 찾아낸건가?  
#STARTLINK   A -> I -> N ->  어떤것 순서대로 뽑아냈는지를 하나하나 생각해봤어야? 
#A는 무엇인가  문자열에서 최소값 I는? 그다음 최소값? 그 오른쪽에 있는 그다음 최소값이어야 하네 
# 그 오른쪽 문자열을 잘라내서 그 최소값을 찾아야하네  문자열 최소값 기준 오른쪽으로 잘라내려면 
# 최소값의 인덱스도 알아야 겠네 그럼 N은? 이런식으로 해가지고 근데 
#나는 답을 한번 봤으니까 보이지 문제 많이 풀다보면 보이려나 
arr = list(input())
result = [""] * len(arr)

def solution(start, arr):
    if not arr:
        return
    minVal = min(arr)
    minIdx = arr.index(minVal)

    result[start + minIdx] = minVal
    print("".join(result))

    solution(start + minIdx + 1, arr[minIdx + 1:])

    solution(start, arr[:minIdx])

solution(0,arr)

