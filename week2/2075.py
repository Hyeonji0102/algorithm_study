'''
다시 풀어볼 것
참고 링크: https://velog.io/@highcho/Algorithm-baekjoon-2075

import sys, heapq
input = sys.stdin.readline

N = int(input())
q = []
for i in range(N):
    num_list = list(map(int, input().split()))

    # q에 아무것도 없는 첫번째 입력의 경우
    if not q:
	for num in num_list:
	# min_heap 구조로 q 채우기
    	    heapq.heappush(q, num)
    else:
        # q에 값이 있을 경우, 늘 q의 길이를 n으로 유지
	for num in num_list:
            # q 최솟값보다 현재 숫자가 클 경우, n번째로 큰 수가 바뀌어야 함
            if q[0] < num:
                # 현재 숫자를 push
		heapq.heappush(q, num)
		# 기존 최솟값 pop
		heapq.heappop(q)
print(q[0])
'''
