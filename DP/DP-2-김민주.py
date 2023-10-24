# 점화식을 그림을 통해 발굴하는 것이 좋음
# 출처: https://velog.io/@real-bird/Python-2n-타일링-2-백준-11727

n = int(input())

# 여기서의 dp는 n별 사각형 수 저장 리스트
rectangular = [0] * 1001
rectangular[1] = 1

if n >= 2:
    rectangular[2] = 3
    for i in range(3, n+1):
        rectangular[i] = (rectangular[i-2]*2) + rectangular[i-1]

print(rectangular[n] % 10_007)
