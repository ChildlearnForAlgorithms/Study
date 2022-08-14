lst=[]
n=int(input())
for _ in range(n):
    a=int(input())
    lst.append(a)

for i in range(n):
    for j in range(n-1,i,-1):
        if lst[j-1]>lst[j]:
            lst[j-1],lst[j]=lst[j],lst[j-1]
for elem in lst:
    print(elem)