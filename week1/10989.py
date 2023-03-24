# 메모리 제한으로 인해 sort 대신 sys 모듈을 import 

import sys

N = int(sys.stdin.readline())
a = [0] * 10001

for i in range(N):
    k = int(sys.stdin.readline())
    # array에 k가 들어온 개수를 확인
    a[k] += 1

for i in range(10001):
    # 숫자가 들어온 경우에 한하여
    if a[i] != 0:
        # array에 들어온 개수만큼 값을 출력
        for j in range(a[i]):
            print(i)
