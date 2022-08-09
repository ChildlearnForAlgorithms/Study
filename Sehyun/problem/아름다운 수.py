n=int(input())
answer=[]
cnt=0
def selection(num):
    global cnt
    if num==n:
        if beautiful_num(answer):
            cnt+=1
        return
    for i in range(1,5):
        answer.append(i)
        selection(num+1)
        answer.pop()


def beautiful_num(answer):
    i=0
    while i<n:
        if i+answer[i]-1>=n:
            return False
        for j in range(i,i+answer[i]):
            if answer[j]!=answer[i]:
                return
        i+=answer[i]
    return True

selection(0)
print(cnt)