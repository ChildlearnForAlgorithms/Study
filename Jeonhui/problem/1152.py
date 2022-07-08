s=input().strip()
s1=s.split(' ')
while '' in s1:
    s1.remove('')
print(len(s1))