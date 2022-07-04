s=input()
result=[-1 for i in range(26)]

for i in range(len(s)):
    pos=ord(s[i])-ord('a')
    result[pos]=i

for j in range(26):
    print(result[j],end=' ')