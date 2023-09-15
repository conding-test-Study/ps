#전에 답지 보고 풀었던 문제 ..
#문자열 정렬할때 앞에 글자 아스키 값이 작은것 순서로 정렬된다..

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
    return answer
