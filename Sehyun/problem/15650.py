n,m=map(int,input().split())
combination=[]

def print_combination():
    for elem in combination:
        print(elem,end=' ')
    print()

def find_combination(curr_num,cnt):
    if curr_num==n+1:
        if cnt==m:
            print_combination()
        return
    combination.append(curr_num)
    find_combination(curr_num+1,cnt+1)
    combination.pop()

    find_combination(curr_num+1,cnt)

find_combination(1,0)
