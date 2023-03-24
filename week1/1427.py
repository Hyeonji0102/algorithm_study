N = int(input())
a = []
a = list(map(int, str(N)))
a.sort(reverse = True)
for i in a:
    print(i, end='')
