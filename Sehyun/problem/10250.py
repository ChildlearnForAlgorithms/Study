T=int(input())
for i in range(T):
    lst = []
    H,W,N=map(int,input().split())
    if N%H==0:
        lst.append(str(H))
        if N/H<10:
            n='0'+str(N//H)
            lst.append(n)
        else:
            lst.append(str(N//H))
        result="".join(lst)
        print(result)

    elif N%H!=0:
        lst.append(str(N % H))
        if N // H+1 < 10:
            n = '0' + str(N // H+1)
            lst.append(n)
        else:
            lst.append(str(N // H+1))
        result = "".join(lst)
        print(result)












