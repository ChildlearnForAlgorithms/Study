import sys

n=int(sys.stdin.readline())
lst=[]

for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    lst.append([a,b])

lst.sort(key=lambda x:x[1])

pos=lst[0][1]

