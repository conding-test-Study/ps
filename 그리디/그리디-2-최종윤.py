# 마지막 1111처리하는거떄문에 틀림

import sys

s = input()

#K가 나왔을 때 앞에 M이랑 합쳐서 변환 -> 최대, 분리해서 변환-> 최소
idx = 0
start = 0
e = 0
maxMK = ""
minMK = ""
while start < len(s):

#1. s = s[start:] K 앞에걸 버린다.
#2. e = s[start:].find  + start -> e를 못찾았을 때
    #-1 + start가 되버림 양수가되버림
    # 찾은 경우에만 K가 있는 경우에만 더해준다.
    e = s[start:].find('K')
    
    if e >= 0:
        e += start
        maxMK += str(5 * 10 ** (e - start))
        #if M이 없다면
        if e - start == 0:
            minMK += "5"
        else:
            minMK += str(10 ** (e - start - 1))
            minMK += str(5)

# 끝에 K가 없다면? e == -1 -> start : len(s) - 1
    else:
        e = len(s) - 1
        maxMK += str(10 ** (e - start))
        minMK += str(10 ** (e - start))

    start = e + 1
    
print(maxMK)
print(minMK)

#  답지확인
import sys
 
w = sys.stdin.readline().strip()
Max = Min = ""
m = 0
for i in range(len(w)):
    if w[i] == "M":
        m += 1
    elif w[i] == "K":
        if m:
            Min += str(10 ** m + 5)
            Max += str(5 * (10 ** m ))
        else:
            Min += "5"
            Max += "5"
        m = 0
if m:
    Min += str(10 ** (m - 1))
    while m:
        Max += "1"
        m -= 1
print(Max)
print(Min)
