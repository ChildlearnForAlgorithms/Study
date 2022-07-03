n=int(input())
a=input()
lst=[]
for i in range(n):
    lst.append(a[i])
sum=0
for j in range(n):
    sum+=int(lst[j])

print(sum)
