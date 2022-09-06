import sys

n=int(sys.stdin.readline())

def factorial(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n*factorial(n-1)

ans=factorial(n)
ans=list(str(ans))
cnt=0

for i in range(len(ans)-1,len(ans)//2,-1):
    if ans[i]=='0':
        cnt+=1
    else:
        break

print(cnt)