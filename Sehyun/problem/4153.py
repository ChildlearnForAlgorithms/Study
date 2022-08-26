while True:
    lst = []
    x,y,z=map(int,input().split())
    lst.append(x)
    lst.append(y)
    lst.append(z)
    if x==0:
        break
    else:
        longest=max(x,y,z)
        lst.remove(longest)
        ans=lst[0]*lst[0]+lst[1]*lst[1]
        if longest*longest==ans:
            print('right')
        else:
            print('wrong')
