n,m=map(int,input().split())

def count(n,k):
    num=0
    while n!=0:
        n=n//k
        num+=n
    return num

ans=min(count(n,2)-count(n-m,2)-count(m,2),count(n,5)-count(n-m,5)-count(m,5))

print(ans*1)