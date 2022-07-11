n=int(input())
def group(s):
    lst=[]
    lst.append(s[0])
    for i in range(1,len(s)):
        if s[i-1]!=s[i]:
            if s[i] not in lst:
                lst.append(s[i])
            else:
                return False
#
count=0
for j in range(n):
    s=input()
    if group(s)!=False:
        count+=1

print(count)



