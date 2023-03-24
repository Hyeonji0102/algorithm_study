N = int(input())
a = []

for i in range(N):
    x, y = map(int, input().split())
    y, x = x, y
    a.append([x,y])

a.sort()

for i in range(N):
    print(a[i][1], a[i][0])
    
