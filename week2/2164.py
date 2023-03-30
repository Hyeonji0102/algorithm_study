'''
collections의 deque를 사용하여 연산의 속도를 향상시킬 것
양 끝에서 list보다 훨씬 빠른 연산 속도를 가짐.
'''

import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(N):
    queue.append(i+1)
    
while (len(queue) != 1):
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])
