import sys

def quick_select(A,k):
    p=A[0]
    S,M,L=[],[],[]
    M.append(p)
    for x in A:
        if x<p:S.append(x)
        elif x>p:L.append(x)
        else:
            M.append(x)
    if len(S)>=k:
        return quick_select(S,k)
    elif len(S)+len(M)<k:
        return quick_select(L,k-len(S)-len(M))
    else:
        return p

A=list(map(int,sys.stdin.readline().split()))

small=quick_select(A,1)

if A.index(small)==0:
    print(0)
else:
    print(len(A)-A.index(small))