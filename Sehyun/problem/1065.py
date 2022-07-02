def sequence(n):
    cnt = 0
    for i in range(1,int(n)+1):
        if i<100:
            cnt+=1
        elif i==1000:
            cnt+=0
        elif i>=100:
            i=str(i)
            if int(i[0])+int(i[2])==2*int(i[1]):
                cnt+=1
            else:
                cnt+=0

    return cnt
#먕
n=input()
print(sequence(n))

