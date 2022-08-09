n,m,k=map(int,input().split())
lst=list(map(int,input().split()))
order=[]
count=0
last=[]
def select(cnt):
    global count
    if cnt==n:
        game()
        last.append(count)
        return
    for i in range(1,k+1):
        order.append(i)
        select(cnt+1)
        order.pop()
    return


def game():
    global count
    result = [1] * (k + 1)
    count=0
    for i in range(n):
        result[order[i]]+=lst[i]
    for i in range(1,k+1):
        if result[i]>=m:
            count+=1
    return count

select(0)
print(max(last))