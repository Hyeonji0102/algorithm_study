'''
stack을 활용하여 괄호 판별을 위한 반복문 작성하기
- 문자열을 한 글자씩 검사해서 여는 괄호면 stack에 넣고, 닫는 괄호이면 stack을 pop()
- pop()할 원소가 없다면 열지도 않은 괄호를 닫은 것 -> 반복문 탈출
- 모든 검사가 끝난 후 stack에 원소가 남아있으면 여는 괄호가 모두 닫히지 않은 것 -> False
'''

T = int(input())
for _ in range(T):
    stack = []
    a = input()
    VPS = True

    for i in a:
        if i == '(':
            stack.append('(')
        if i == ')':
            if stack:
                stack.pop()
            else:
                VPS = False
                break
    if not stack and VPS:
        print('YES')
    elif stack or not VPS:
        print('NO')
