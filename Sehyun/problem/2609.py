a,b=map(int,input().split())
small=min(a,b)
factor=1
for i in range(2,small+1):
    if a%i==0 and b%i==0:
        factor=i
    else:
        continue
multiple=(a//factor)*(b//factor)*factor
print(factor)
print(multiple)