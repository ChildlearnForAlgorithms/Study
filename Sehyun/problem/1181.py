n=int(input())
lst=[]
for i in range(n):
    a=input()
    if a not in lst:
        lst.append(a)
lst.sort(key=lambda x:(len(x),x))
for elem in lst:
    print(elem)