n=int(input())

memo=[-1]*(n+1)

def fibonacci(n):
    if memo[n]!=-1:
        return memo[n]
    if n==1 or n==2:
        return 1
    memo[n]=fibonacci(n-1)+fibonacci(n-2)
    return memo[n]

print(fibonacci(n))