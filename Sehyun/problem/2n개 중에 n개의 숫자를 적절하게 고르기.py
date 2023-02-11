n=int(input())

lst=list(map(int,input().split()))
select_lst=[]
sub_lst=[]

if n%2==0:
    while len(lst)>n:
        select_lst.append(max(lst))
        lst.remove(max(lst))
        select_lst.append(min(lst))
        lst.remove(min(lst))
    print((abs(sum(sub_lst)-sum(select_lst))))

if n%2==1:
    while len(lst)>n+1:
        select_lst.append(max(lst))
        lst.remove(max(lst))
        select_lst.append(min(lst))
        lst.remove(min(lst))
    if sum(lst)>sum(select_lst):

