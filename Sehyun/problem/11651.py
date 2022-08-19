n=int(input())
P=[]

for _ in range(n):
    a=tuple(map(int,input().split()))
    P.append(a)

P.sort(key=lambda a:(a[1],a[0]))


for i in range(n):
    print(P[i][0],P[i][1])