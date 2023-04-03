import sys
import heapq

N = int(sys.stdin.readline())
minheap = []

for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(minheap):
            print(heapq.heappop(minheap))
        else:
            print(0)
            
    else:
        heapq.heappush(minheap, n)
