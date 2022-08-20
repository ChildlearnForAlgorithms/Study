import sys
n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    x,y=sys.stdin.readline().split()
    x=int(x)
    lst.append((x,y))
second_lst=[]
for i,tuple in enumerate(lst):
    second_lst.append((i,tuple))
second_lst.sort(key=lambda x:(x[1][0],x[0]))

for i in range(n):
    print(second_lst[i][1][0],second_lst[i][1][1])