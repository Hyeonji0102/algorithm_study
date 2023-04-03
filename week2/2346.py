'''
다시 풀 것 
참고링크: https://velog.io/@hygge/Python-백준-2346-풍선-터뜨리기-deque
'''

import sys
from collections import deque

N = int(sys.stdin.readline())

dq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for i in range(N):
    p = dq.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        dq.rotate(-(p[1] - 1))
    else:
        dq.rotate(-p[1])
