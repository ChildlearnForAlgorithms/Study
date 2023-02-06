n=int(input())
lst=[]
visited=[False]*(n+1)

def print_all():
    for elem in lst:
        print(elem,end=" ")
    print()

def choose(curr_num):
    if curr_num==n+1:
        print_all()
        return

    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i]=True
        lst.append(i)
        choose(curr_num+1)
        lst.pop()
        visited[i]=False

choose(1)


