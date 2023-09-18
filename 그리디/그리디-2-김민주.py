# 방법론 자체는 여타 해답과 비슷하나, 지속적 오답 발생으로 인해 조금 더 이유를 알아볼 예정.

letters = input()

max_n = ''
min_n = ''

D = []

for l in letters:
    if l == 'M':
        D.append(l)
    else:
        print("리스트: ", D)

        if D.count('M') >= 1:
            number = 10 ** D.count('M')

            max_n += str(number * 5)
            min_n += str(number + 5)

        else:
            max_n += str(5)
            min_n += str(5)

        print("최댓값 중간: ", max_n)
        print("최솟값 중간: ", min_n)

        D.clear()

if len(D) != 0:
    # number = 10 ** (D.count('M') - 1)
    min_n += str(10 ** (D.count('M') - 1))
    max_n += str(D.count('M') - 1)

print(max_n)
print(min_n)
