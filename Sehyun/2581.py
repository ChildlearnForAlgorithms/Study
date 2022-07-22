m=int(input())
n=int(input())

def prime(a):
    cnt=0
    for i in range(1,a+1):
        if a%i==0:
            cnt+=1
    return cnt
lst=[]
for i in range(m,n+1):
    if prime(i)==2:
        lst.append(i)

if len(lst)==0:
    print(-1)
else:
    print(sum(lst),lst[0])
