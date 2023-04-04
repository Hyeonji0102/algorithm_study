from collections import deque

N = int(input())
pizza = list(map(int, input().split()))
done = [0 for i in range(N)]
dq = deque()
cnt = 0

for i in range(N):
    dq.append([i,0])

while dq:
    num, get = dq.popleft()
    cnt += 1
    get += 1
    if pizza[num] == get:
        done[num] = cnt
    else:
        dq.append([num, get])

done = map(str, done)
print(' '.join(done))
