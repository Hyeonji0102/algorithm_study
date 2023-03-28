'''
시간초과를 해결하기 위해 dictionary를 사용할 것
dictionary의 value에 접근하는 시간복잡도는 O(1)

같은 수는 같은 좌표값을 가지기 때문에 집합(set)을 통해 중복값을 제거할 것
'''

import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

#a를 set으로 만들고 정렬
sorted_a = sorted(set(a))

# 딕셔너리에 '숫자: sorted_a에서의 인덱스'로 저장
dict_a = {sorted_a[i]: i for i in range(len(sorted_a))}

for i in a:
    print(dict_a[i], end=' ')
