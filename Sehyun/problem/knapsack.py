def knapsack(i,size):
    global MP
    if i>=n or size<=0:
        return
    p,s=0,0
    for j in range(i):
        if x[j]==1:
            p+=P[j][1]
            s+=P[j][0]
    if P[i][0]<=size:
        B=fractional_knapsack(i+1,size-P[i][0])
        if MP<p+P[i][1]+B:
            x[i]=1
            MP=max(MP,p+P[i][1])
            knapsack(i+1,size-P[i][0])
    B=fractional_knapsack(i+1,size)
    if MP<p+B:
        x[i]=0
        knapsack(i+1,size)

def fractional_knapsack(i,size):
    if size<0:
        return
    p,s=0,0
    P.sort(key=lambda x: -x[1] / x[0])
    for j in range(i,n):
        if s+P[j][0]<=size:
            p += P[j][1]
            s += P[j][0]
        else:
            p+=(size-s)*(P[j][1]/P[j][0])
            s+=(size-s)
            break
    return p



k=int(input())
n=int(input())
n_size=list(map(int,input().split()))
n_profit=list(map(int,input().split()))
x = [0 for _ in range(n)]
MP=0
P=[]

for i in range(n):
    P.append((n_size[i],n_profit[i]))
knapsack(0,k)
print(MP)