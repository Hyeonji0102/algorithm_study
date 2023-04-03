from collections import deque

N = int(input())
dq = deque()

dq.appendleft(N)

for i in range(N - 1, 0, -1):
    dq.appendleft(i)
    for j in range(i):
        dq.appendleft(dq.pop())

print(*dq)
