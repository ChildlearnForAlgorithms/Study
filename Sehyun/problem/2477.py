k = int(input())
lst=[list(map(int,input().split())) for _ in range(6)]
w=0;w_index=0
h=0;h_index=0
for i in range(6):
    if lst[i][0]==1 or lst[i][0]==2:
        if w<lst[i][1]:
            w=lst[i][1]
            w_index=i
    elif lst[i][0]==3 or lst[i][0]==4:
        if h<lst[i][1]:
            h=lst[i][1]
            h_index=i
subW=abs(lst[(w_index-1)%6][1]-lst[(w_index+1)%6][1])
subH=abs(lst[(h_index-1)%6][1]-lst[(h_index+1)%6][1])
print((w*h-subH*subW)*k)
