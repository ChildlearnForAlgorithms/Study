import math

m,n=map(int,input().split())

def prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True

for i in range(m,n+1):
    if prime(i)==True:
        print(i)