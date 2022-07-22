n=int(input())
i=2
if n==1:
    print()
while n!=1:
    if n%i!=0:
        i+=1
    else:
        n//=i
        print(i)