n=int(input())
answer=[]
visited=[False]*(n+1)

def print_answer():
    for element in answer:
        print(element,end=' ')
    print()
    return

def choose(curr_num):
    if curr_num==1:
        print_answer()
        return
    for i in range(n,0,-1):
        if visited[i]:
            continue
        visited[i]=True
        answer.append(i)
        choose(curr_num-1)
        answer.pop()
        visited[i]=False

choose(n+1)