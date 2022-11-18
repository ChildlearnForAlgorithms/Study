n = int(input())
lst=list()

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,"f"))
    lst.append((b, "l"))

lst.sort(key=lambda x:(x[0],x[1]))


cnt,max_cnt=0,0

for i in range(n):
    if lst[i][1]=="f":
        cnt+=1
    elif lst[i][1]=="l":
        max_cnt = max(cnt, max_cnt)
        cnt-=1


print(max_cnt)