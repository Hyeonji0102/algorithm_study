'''
문제 이해 및 참고 링크: https://feca.tistory.com/7
아홉 난쟁이 키의 합 - 가짜 난쟁이들의 키의 합 = 100
'''

import sys

hgt = []
for i in range(9):
    hgt.append(int(sys.stdin.readline()))

hsum = sum(hgt)
one, two = 0, 0

for i in range(9):
    for j in range(i+1, 9):
        if (hgt[i] + hgt[j] == hsum - 100):
            one, two = hgt[i], hgt[j]
            break

hgt.remove(one)
hgt.remove(two)
hgt.sort()

for i in hgt:
    print(i)
