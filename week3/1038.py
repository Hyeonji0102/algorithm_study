'''
참고 링크:
- https://velog.io/@sugyeonghh/백준-1038-감소하는-수Python
- https://fre2-dom.tistory.com/487
'''

import sys
from itertools import combinations

n = int(sys.stdin.readline())
ans = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        ans.append(int("".join(map(str, num))))

ans.sort()
if len(ans) > n:
    print(ans[n])
else:
    print(-1)
