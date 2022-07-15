num=int(input())
for i in range(num):
    a=input().split(' ')
    b=a[0]
    c=a[1]
    for j in range(len(c)):
        print(c[j]*int(b),end='')
    print()