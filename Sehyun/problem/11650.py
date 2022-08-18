n=int(input())
P=[]

for _ in range(n):
    a=tuple(map(int,input().split()))
    P.append(a)

P.sort(key=lambda a:(a[0],a[1]))


for i in range(n):
    print(P[i][0],P[i][1])
