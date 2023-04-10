'''
참고 링크
- https://ji-gwang.tistory.com/245
- https://data-flower.tistory.com/97
반복문을 중첩시켜 사탕을 바꿨을 때 각각의 케이스를 전부 고려하도록 할 것
사탕색을 바꾸고 개수를 계산한 다음 색을 다시 원 상태로 돌려 놓아야 함!
'''

N = int(input())
arr = []
for i in range(N):
    clr = list(map(str, input()))
    arr.append(clr)

mxcnt = 0

def width():
    global mxcnt

    for k in range(N):
        cntrow = 1
        for l in range(N-1):
            if arr[k][l] == arr[k][l+1]:
                cntrow +=1
                mxcnt = max(mxcnt, cntrow)
            else:
                cntrow = 1

def height():
    for k in range(N):
        global mxcnt

        cntcol = 1
        for l in range(N-1):
            if arr[k][l] == arr[l+1][k]:
                cntcol += 1
                mxcnt = max(mxcnt, cntcol)
            else:
                cntcol = 1

for i in range(N):
    for j in range(N-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            width()
            height()
            arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            width()
            height()
            arr[j+1][i], arr[j][i] = arr[j][i], arr[j+1][i]

print(mxcnt)
