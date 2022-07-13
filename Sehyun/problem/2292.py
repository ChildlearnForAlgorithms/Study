n=int(input())
a=1
i=1

if n==1:
    print(1)

while n>a:
    a+=6*i
    i+=1
    if n<=a:
        print(i)
        break

