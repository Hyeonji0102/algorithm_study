n_list = []
for i in range(5):
  k = int(input())
  n_list.append(k)

n_list.sort()

print(int(sum(n_list) / len(n_list)))
print(n_list[2])
