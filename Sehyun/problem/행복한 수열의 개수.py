n,m=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

result=0

for i in range(n):
    cnt1 = 1
    max_cnt1=1
    for j in range(n-1):
        if grid[i][j]==grid[i][j+1]:
            cnt1+=1
        else:
            cnt1=1
        max_cnt1=max(max_cnt1,cnt1) #중요
    if max_cnt1>=m:
        result+=1

for i in range(n):
    cnt2 = 1
    max_cnt2=1
    for j in range(n-1):
        if grid[j][i]==grid[j+1][i]:
            cnt2+=1
        else:
            cnt2=1
        max_cnt2 = max(max_cnt2, cnt2)
    if max_cnt2 >= m:
        result += 1

print(result)
'''
5 3
1 2 3 4 5
6 6 6 1 2
3 4 5 6 6
7 8 9 9 9
1 2 3 4 5'''