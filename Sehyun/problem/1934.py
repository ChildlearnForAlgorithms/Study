def euclidean(a,b):
    if a<b:
        temp=a
        a=b
        b=temp
    while b!=0:
        n=a%b
        a=b
        b=n
    return a

T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    factor=euclidean(a,b)
    answer=(a//factor)*(b//factor)*factor
    print(answer)
