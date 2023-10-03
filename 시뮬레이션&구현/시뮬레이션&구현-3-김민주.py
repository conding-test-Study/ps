# 원래 풀이
# 예시 답안 3번 풀이법을 생각 못 했음.

import sys
string = input()

letters = []

for i in range(len(string)):
    letters.append([string[i], i, ord(string[i])])

letters.sort(key=lambda x: x[2])
print(letters)


# 알파벳 + 위치 순으로 출력해주는 함수 만들기
# 알파벳 순으로 + 위치에 맞춰 출력
result = ['' for _ in range(len(string))]

result[letters[0][1]] = letters[0][0]
std = letters[0][1]
cnt = len(letters)

i = 0
while letters:
    if i < cnt:
        if letters[i][1] >= std:
            result[letters[i][1]] = letters[i][0]
            print(''.join(result))
            letters[i] = []
            i += 1
        else:
            i += 1

    else:
        if i < cnt*2:
            if len(letters[i-cnt]) > 0:
                result[letters[i-cnt][1]] = letters[i-cnt][0]
                print(''.join(result))
                letters[i-cnt] = []
                i += 1
            else:
                i += 1
        else:
            break

# 모범답안 (출처: https://wooono.tistory.com/609)

# 문자열 입력
words = sys.stdin.readline().rstrip()

# 입력 문자열, 입력 문자열의 시작 인덱스
# ord 메소드 활용 x, min을 이용하여 사전상으로 가장 앞에 도달할 문자를 판별


def solution(input_words, start_idx):

    # 전역 변수 수정 권한
    global result

    # 입력 배열이 비어있으면 리턴
    if input_words == "":
        return

    # 입력 문자열에서 가장 작은 문자 탐색
    min_char = min(input_words)
    # 가장 작은 문자의 인덱스 탐색
    min_char_idx = input_words.index(min_char)

    # 알파벳 위치(입력 문자열의 시작 인덱스 + 가장 작은 문자의 인덱스)에 알파벳 저장
    result[start_idx + min_char_idx] = min_char

    # 결과 배열 출력
    print(''.join(result))

    # 해당 문자 기준 뒷 문자열에 대해 위 함수 실행
    solution(input_words[min_char_idx + 1:], start_idx + min_char_idx + 1)

    # 해당 문자 기준 앞 문자열에 대해 위 함수 실행
    solution(input_words[:min_char_idx], start_idx)


# 결과 배열
result = [''] * len(words)

# 함수 호출 (입력 문자열, 입력 문자열의 시작 인덱스)
solution(words, 0)
