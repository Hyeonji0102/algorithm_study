import sys
N = int(sys.stdin.readline())
a = []

for i in range(N):
    a.append(list(sys.stdin.readline().split()))

a.sort(key = lambda x: int(x[0]))

for i in range(N):
    print(a[i][0], a[i][1])
