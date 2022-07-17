A,B,V=map(int,input().split())
if A>=V:
    print(1)
else:
    print((V-B-1) // (A-B)+1)