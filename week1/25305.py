N, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()

cut = scores[-k]
print(cut)
    
