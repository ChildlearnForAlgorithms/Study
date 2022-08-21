import sys
n=int(sys.stdin.readline())
own=set(map(int,sys.stdin.readline().split()))
m=int(input())
card=list(map(int,sys.stdin.readline().split()))
card_list=[]
for i in range(m):
    if card[i] in own:
        card_list.append(1)
    else:
        card_list.append(0)
for elem in card_list:
    print(elem,end=' ')