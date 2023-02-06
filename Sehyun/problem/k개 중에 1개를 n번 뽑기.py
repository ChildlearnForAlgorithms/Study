k,n=map(int,input().split())

lst=[]

def print_ans():
    for elem in lst:
        print(elem,end=" ")
    print()

def choose(curr_num):
    if curr_num==n+1:
        print_ans()
        return

    for i in range(1,k+1):
        lst.append(i)
        choose(curr_num+1)
        lst.pop()

choose(1)