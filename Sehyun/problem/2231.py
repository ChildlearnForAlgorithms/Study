n=int(input())
result_list=[]
for i in range(1,n):
    result=i
    lst=list(map(int,str(i)))
    result+=sum(lst)
    if result==n:
        result_list.append(i)

if len(result_list)==0:
    print(0)
else:
    print(min(result_list))
