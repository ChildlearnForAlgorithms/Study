result=[]
alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input()
for i in range(26):
    if alph[i] in s:
        pos=s.find(alph[i])
        result.append(pos)
    else:
        result.append(-1)

for j in range(26):
    print(result[j],end=' ')