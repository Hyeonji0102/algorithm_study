'''
이진 탐색 기법 사용

이진 탐색 함수를 돌면서 숫자가 존재하면 1을, 그렇지 않으면 0을 return 받도록 한다.
'''

import sys
N = int(sys.stdin.readline())
own = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위한 리스트는 정렬되어야 함
own.sort()

def binary(k, own, start, end):
    while start <= end:
        mid = (start+end) // 2
        if own[mid] == k:
            return 1
        elif own[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in card:
    print(binary(i, own, 0, N-1), end=' ')

