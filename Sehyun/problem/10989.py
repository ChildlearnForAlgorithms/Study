import sys
n=int(sys.stdin.readline())
lst=[0]*10001
for i in range(n):
    lst[int(sys.stdin.readline())]+=1
for i in range(1,10001):
    if lst[i]!=0:
        for _ in range(lst[i]):
            print(i)