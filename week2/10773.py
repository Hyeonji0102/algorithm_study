import sys
K = int(sys.stdin.readline())
a = []

for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        a.pop()

    else:
        a.append(num)

print(sum(a))
