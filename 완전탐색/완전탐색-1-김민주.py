# 단어 1개에서 문자 전부 뽑기 & 단어 여러개에서 문자 뽑기 함수 분리하여 생성
# 단어 여러개에서 문자 뽑는 케이스를 정교하게 구상하는 데에 어려움 있음
import sys
from collections import Counter
T = input()
N = int(input())
books = []
for _ in range(N):
    books.append(input().split())

print(books)


def count_one_book(li, target):

    for l in li:
        result = []
        word = l[1]

        for t in target:
            if t in word:
                result.append(t)

        # print(result)

        if len(result) == len(target):
            return int(l[0])

    return False


def count_many_books(li, target):

    price_result = []
    word_result = ''

    for l in li:
        word = l[1]

        for t in target:
            if t in word and t not in word_result:
                price_result.append(int(l[0]))
                word_result += t

    if len(word_result) == len(target):
        return sum(price_result)


res = count_one_book(books, T)
res_many = count_many_books(books, T)
print(res)
print(res_many)


# 참고 코드 (출처: https://pinopino.tistory.com/entry/%EB%B0%B1%EC%A4%80-16508-%EC%A0%84%EA%B3%B5%EC%B1%85)

#  문자열을 만들 수 있는지 확인하기

def check(alphabets, string):
    for w in string:
        # 없는 알파벳이거나, 더이상 추가할 수 없다면 실패
        if w not in alphabets or alphabets[w] == 0:
            return False
        else:
            alphabets[w] -= 1   # 알파벳 숫자 줄이기
    return True


T = input()
N = int(input())
books = []              # 책 리스트 (가격, 책제목의 알파벳 개수)
for _ in range(N):
    price, title = input().split()
    books.append((int(price), Counter(title)))

answer = sys.maxsize

# 00..0 ~ 11...1 까지 각 전공책이 포함 되고 포함되지 않는 경우의 수 확인
for i in range(1 << N):
    price = 0
    alphabets = Counter()      # 전공책의 알파벳들

    for j in range(N):
        if (i & 1 << j) != 0:          # j 번째 전공책이 포함된 경우
            price += books[j][0]        # 가격 더하고
            alphabets += books[j][1]    # 문자열 더하기

    if check(alphabets, T):  # 문자열을 만들 수 있다면 최솟값 저장
        answer = min(answer, price)

print(-1) if answer == sys.maxsize else print(answer)
