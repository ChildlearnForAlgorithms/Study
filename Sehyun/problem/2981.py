import sys
from math import gcd
from math import sqrt

n=int(sys.stdin.readline())
num_list=list(int(sys.stdin.readline()) for _ in range(n))
num_list.sort()
interval=[]
answer=[]

for i in range(1,n):
    interval.append(num_list[i]-num_list[i-1])

prev=interval[0]
for i in range(1,len(interval)):
    prev=gcd(prev,interval[i])

for i in range(2,int(sqrt(prev))+1):
    if prev%i==0:
        answer.append(i)
        answer.append(prev//i)
answer.append(prev)
answer=list(set(answer))
answer.sort()
for elem in answer:
    print(elem,end=' ')