import sys

n,k=map(int,sys.stdin.readline().split())
lst=list(map(int,input().split()))
answer=[]
answer.append(sum(lst[:k]))

for i in range(1,n-k+1):
    answer.append(answer[i-1]-lst[i-1]+lst[i+k-1])

print(max(answer))



