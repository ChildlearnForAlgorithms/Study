n=int(input())
lst=[]
for i in range(n):
    a,b=map(int,input().split())
    lst.append((a,b))
result = []
for i in range(n):
    num = 0
    for j in range(n):
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            num+=1
    result.append(num+1)

for i in range(n):
    print(result[i],end=" ")

'''
5
55 185
58 183
88 186
60 175
46 155'''