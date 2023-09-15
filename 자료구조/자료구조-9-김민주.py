# 해시 자료구조를 이용하되, hash 내장함수는 이용하지 않음
# 모범 풀이 활용 (참고: https://codingpractices.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%8B%9C-Hash-%ED%95%B4%EC%8B%B1-Hashing-%EB%AC%B8%EC%A0%9C%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)

def solution(phone_book):
    answer = True
    hash = {}

    # 해시 딕셔너리에 전화번호 집어넣기
    for phone in phone_book:
        hash[phone] = 1

    print(hash)

    # 각 전화번호의 자릿수를 누적시키며, 누적 결과가 한 번이라도 해시 딕셔너리에 있다면 answer = False 처리해주기
    for phone in phone_book:

        num = ''
        for p in phone:
            num += p
            if num in hash and num != p:
                answer = False

    return answer


print(solution(["119", "97674223", "1195524421"]))
