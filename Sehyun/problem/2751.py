import sys
n=int(input())
L=[]
for _ in range(n):
    a=int(sys.stdin.readline())
    L.append(a)

for elem in sorted(L):
    print(elem)

