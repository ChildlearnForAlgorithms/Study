import sys
n=int(sys.stdin.readline())
cnt1=0
def fib(n):
    global cnt1
    if n==1 or n==2:
        cnt1+=1
        return 1
    else:
        return fib(n-1)+fib(n-2)

f=[0]*(n+1)
cnt2=0
def fibonacci(n):
    global cnt2
    f[1]=1;f[2]=2
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
        cnt2+=1
    return f[n]
fib(n)
fibonacci(n)
print(cnt1,cnt2)
