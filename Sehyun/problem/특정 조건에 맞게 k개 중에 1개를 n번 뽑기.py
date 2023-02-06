k,n=map(int,input().split())

lst=[]

def print_all():
    for elem in lst:
        print(elem,end=" ")
    print()

def choose(curr_num):
    if curr_num==n+1:
        print_all()
        return

    for i in range(1,k+1):
        if len(lst)>=2 and (lst[-2]==lst[-1] and lst[-1]==i):
            continue

        else:
            lst.append(i)
            choose(curr_num+1)
            lst.pop()

choose(1)