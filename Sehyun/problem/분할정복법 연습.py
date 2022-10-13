import sys

lst=list(map(int,sys.stdin.readline().split()))
lst_s=sorted(lst)
print(lst_s.index(lst[0]))