import itertools
n,m=map(int,input().split())
lst=list(map(int,input().split()))
comb=list(itertools.combinations(lst,3))
sum_list=[]
for i in range(len(comb)):
    sum=0
    for j in range(3):
        sum+=comb[i][j]
    sum_list.append(sum)
result=[]
for i in range(len(sum_list)):
    if sum_list[i]<=m:
        result.append(sum_list[i])

print(max(result))