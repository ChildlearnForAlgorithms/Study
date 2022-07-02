numList=[0 for i in range(10001)]

def D(n):
    num=int(n)
    for i in range(len(n)):
        num+=int(n[i])
    if num<10001:
        numList[num]=num

for j in range(10001):
    D(str(j))

pos=[str(i) for i in range(1,len(numList)) if numList[i]==0]

print("\n".join(pos))