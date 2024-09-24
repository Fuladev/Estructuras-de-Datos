N,Q=list(map(int,input().split()))

X=list(map(int,input().split()))

E={}

if len(X)==N:
    for i in X:
        if i not in E.keys():
            E[i]=1
        else:E[i]+=1
    for _ in range(Q):
        P=list(map(int,input().split()))
        if P[0] in E.keys() and E[P[0]]>=P[1]:print('SI')
        else:print('NO')