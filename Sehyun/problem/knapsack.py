import sys

k=int(sys.stdin.readline())
n=int(sys.stdin.readline())
n_lst=list(map(int,sys.stdin.readline()))
n_profit=list(map(int,sys.stdin.readline()))

maxProfit=0

profit_lst=[]

for i in range(n):
    profit_lst.append(n_profit[i]/n_lst[i])
