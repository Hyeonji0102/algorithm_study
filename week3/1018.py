N,M = map(int,input().split())

brd=[]
cnt=[]
for i in range(N):
    brd.append(input())
    
for a in range(N-7):
    for b in range(M-7):
        w_idx=0
        b_idx=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if brd[i][j]!='W':
                        w_idx+=1
                    else:
                        b_idx+=1
                else:
                    if brd[i][j]!='W':
                        b_idx+=1
                    else:
                        w_idx+=1
                        
        cnt.append(w_idx)
        cnt.append(b_idx)
print(min(cnt))
