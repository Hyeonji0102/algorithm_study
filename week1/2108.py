# 최빈값 구하는 부분 다시 풀 것
'''
from collections import Counter  #collection 모듈 import

cnt = Counter(a).most_common()  #Counter()는 빈도수 구해주는 함수, dictionary 형태로 수와 빈도수가 저장된 배열
max_fq = cnt[0][1]  #최대 빈도수

fq = []  #최대 빈도수를 가진 수를 저장하도록 하는 리스트

#i[1]은 각 수의 빈도수, 이것이 최대 빈도수인 경우에 fq 리스트에 해당 숫자를 추가
for i in cnt:
    if i[1] == max_fq:
        fq.append(i[0])

# 최대빈도수를 가진 수가 1개인 경우에는 첫 번째 숫자를 출력, 그렇지 않으면 정렬후 두번째 인덱스 출력
if len(fq) == 1:
    print(fq[0])
else:
    fq.sort()
    print(fq[1])
'''

import sys

N = int(sys.stdin.readline())
a = []
for i in range(N):
    a.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(a)/N))

# 중앙값
a.sort()
print(a[len(a)//2])

# 최빈값

# 범위
print(max(a)-min(a))
