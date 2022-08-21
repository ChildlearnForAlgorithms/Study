import sys
n,m=map(int,sys.stdin.readline().split())
a=set()
for _ in range(n):
    b=sys.stdin.readline()
    a.add(b)
check=[]
for _ in range(m):
    c=sys.stdin.readline()
    check.append(c)
cnt=0
for i in range(m):
    if check[i] in a:
        cnt+=1

print(cnt)