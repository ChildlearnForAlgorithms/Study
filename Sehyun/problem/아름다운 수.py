n=int(input())

lst=[]

cnt=0
def choose(curr_num):
    global cnt
    if curr_num==n+1:
        if beautiful_num(lst):
            cnt+=1
        return

    for i in range(1,5):
        lst.append(i)
        choose(curr_num+1)
        lst.pop()


def beautiful_num(lst):
    i=0
    while i<n:
        if i+lst[i]>n:
            return False
        for j in range(i,i+lst[i]):
            if lst[i]!=lst[j]:
                return False
        i+=lst[i]
    return True

choose(1)
print(cnt)