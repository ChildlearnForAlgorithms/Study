n=int(input())
lst=[]
visited=[False]*(n+1)

def print_all():
    for elem in lst:
        print(elem,end=" ")
    print()

def select(curr_num):
    if curr_num==n:
        print_all()
        return
    for i in range(n,0,-1):
        if visited[i]:
            continue
        lst.append(i)
        visited[i]=True
        select(curr_num+1)
        lst.pop()
        visited[i]=False
select(0)

