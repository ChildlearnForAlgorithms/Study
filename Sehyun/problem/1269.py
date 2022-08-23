import sys
A,B=map(int,sys.stdin.readline().split())
a=set(list(map(int,sys.stdin.readline().split())))
b=set(list(map(int,sys.stdin.readline().split())))
cnt1=len(a-b)
cnt2=len(b-a)
print(cnt1+cnt2)