s=input()
cralph=['c=','c-','dz=','d-','lj','nj','s=','z=']
count=0

for i in range(len(cralph)):
    for j in range(len(s)-len(cralph[i])+1):
        if cralph[i] in s[j:j+len(cralph[i])]:
            count += s.count(cralph[i])
            s=s.replace(s[j:j+len(cralph[i])]," ")

s=s.replace(" ","")
count+=len(s)
print(count)



