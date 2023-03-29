import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    wd = sys.stdin.readline().split()
    order = wd[0]

    if order == 'push':
        value = wd[1]
        stack.append(value)
        
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif order == 'size':
        print(len(stack))
        
    elif order == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
            
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
