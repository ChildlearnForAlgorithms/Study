n,m=map(int,input().split())
hear=set()
see=set()
for _ in range(n):
    a=input()
    hear.add(a)
for _ in range(m):
    b=input()
    see.add(b)
lst=sorted(list(hear&see))
print(len(lst))
for elem in lst:
    print(elem)