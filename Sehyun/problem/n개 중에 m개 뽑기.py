n,m=map(int,input().split())

lst=[]

def print_all():
    for elem in lst:
        print(elem,end=" ")
    print()

def choose(curr_num,cnt):
    if curr_num==n+1:
        if cnt==m:
            print_all()
        return

    lst.append(curr_num)
    choose(curr_num+1,cnt+1)
    lst.pop()

    choose(curr_num+1,cnt)
choose(1,0)