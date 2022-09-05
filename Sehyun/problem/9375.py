import collections

T=int(input())

for i in range(T):
    n=int(input())
    list_type=[]
    for _ in range(n):
        a,b=input().split()
        list_type.append(b)
    dict_type=collections.Counter(list_type)
    cnt=1
    for k in dict_type:
        cnt*=(dict_type[k]+1)
    print(cnt-1)