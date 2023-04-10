'''
참고 링크: https://woong-gil.tistory.com/6
'''

N = int(input())
res = []
for i in range(1, N+1):
    tmp = [N, i]
    while True:
        val = tmp[-2] - tmp[-1]  # 다음 값은 인덱스 -2에서 -1을 뺀 값
        if val >= 0:             # 이 값이 정수라면 list에 append
            tmp.append(val)
        else:                    # 아니면 break
            break
    if len(tmp) > len(res):   # tmp의 길이가 result보다 클 경우
        res = tmp
print(len(res))
for i in res:
    print(i, end=' ')
