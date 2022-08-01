n,m=map(int,input().split())
row=[]
for i in range(n):
    column=list(input())
    row.append(column)
#다시 칠해야하는 정사각형 개수 구해야 하니까 원소 하나하나 접근
result=[]
for i in range(n-7):
    for j in range(m-7):
        cnt1=0
        cnt2=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if row[a][b]!='W':
                        cnt1+=1
                    else:
                        cnt2+=1
                else:
                    if row[a][b]!='B':
                        cnt1+=1
                    else:
                        cnt2+=1
        result.append(min(cnt1,cnt2))
print(min(result))