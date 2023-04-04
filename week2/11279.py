import sys
import heapq

N = int(sys.stdin.readline())
maxheap = []

for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(maxheap)== 0:
            print(0)
        else:
            print((-1)*heapq.heappop(maxheap))
    else:
        heapq.heappush(maxheap, (-1) * n)
