import sys
N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    wd = sys.stdin.readline().split()
    order = wd[0]

    if order == 'push':
        value = wd[1]
        queue.append(value)
        
    elif order == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
            
    elif order == 'size':
        print(len(queue))
        
    elif order == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
            
    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
