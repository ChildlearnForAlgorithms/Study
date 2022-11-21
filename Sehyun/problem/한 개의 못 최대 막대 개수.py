import sys

n = int(sys.stdin.readline())
lst=list()

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a,"f"))
    lst.append((b, "l"))

lst.sort(key=lambda x:(x[0],x[1]))

cnt,max_cnt=0,0
for i in range(2*n):
    if lst[i][1]=="f":
        cnt+=1
    if lst[i][1]=="l":
        cnt-=1
    max_cnt=max(cnt,max_cnt)

print(max_cnt)