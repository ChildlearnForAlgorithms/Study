import math
sum=0
lst=[]
for _ in range(5):
    a=int(input())
    sum+=a
    lst.append(a)

lst.sort()
print(math.floor(sum/5))
print(lst[2])