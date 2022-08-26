lst_x=[]
lst_y=[]
for _ in range(3):
    x,y=map(int,input().split())
    lst_x.append(x)
    lst_y.append(y)
check_x=[]
for i in range(3):
    if lst_x[i] not in check_x:
        check_x.append(lst_x[i])
    else:
        check_x.remove(lst_x[i])
check_y=[]
for i in range(3):
    if lst_y[i] not in check_y:
        check_y.append(lst_y[i])
    else:
        check_y.remove(lst_y[i])
print(*check_x,*check_y)