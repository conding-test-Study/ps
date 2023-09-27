# 답 구글링함
# 단순한 정렬문제라고 생각하며 접근했으나 그게 아니었음
# 뒷 문자열에 대해 먼저 재귀를 돌리는건 현재 문자가 사전순으로 가장 앞에 있는 문자이므로 뒤부터 탐색해서 현재 문자를 가장 앞으로 보내놔야함

import sys
input = sys.stdin.readline

words = input().rstrip()
def solution(input_words, start_idx):
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

result = [''] * len(words)
solution(words, 0)