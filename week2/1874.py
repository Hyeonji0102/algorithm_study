'''
문제 이해
- stack에 push할 때에는 오름차순으로만 push
- pop한 수를 나열하였을 때, N줄에 걸쳐 입력한 수열과 같아야 함

참고 링크: https://data-flower.tistory.com/98
'''

N = int(input())
stack = []
ans = []
find = True
curr = 1

for i in range(N):
    num = int(input())
    # 입력한 수를 만날 때까지 오름차순으로 push
    while curr <= num:
        stack.append(curr)
        ans.append('+')
        curr += 1
    # stack의 top이 입력한 숫자와 같은 경우, 수열을 만든다
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    # 그렇지 않은 경우는 stack을 만들 수 없다
    else:
        find = False

if not find:
    print('NO')
else:
    for i in ans:
        print(i)
