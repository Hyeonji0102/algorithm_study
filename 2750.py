N = int(input())
n_list = []

for i in range(N):
  k = int(input())
  n_list.append(k)

n_list.sort()

for i in n_list:
  print(i)
