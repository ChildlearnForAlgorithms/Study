from collections import Counter
import sys
n=int(sys.stdin.readline())
lst=[]
for _ in range(n):
    a=int(sys.stdin.readline())
    lst.append(a)
lst.sort()
def average(lst):
    num=sum(lst)/n
    print(round(num))
def median(lst):
    print(lst[n//2])
def mode(lst):
    cnt=Counter(lst).most_common()
    answer=[]
    for i in cnt:
        if i[1]==cnt[0][1]:
            answer.append(i[0])
        else:
            break
    if len(answer)==1:
        print(answer[0])
    else:
        answer.sort()
        print(answer[1])
def scope(lst):
    print(max(lst)-min(lst))
average(lst)
median(lst)
mode(lst)
scope(lst)
