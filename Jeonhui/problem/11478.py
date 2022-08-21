import sys

s = sys.stdin.readline()
d={}
for i in range(1, len(s) + 1):
    for j in range(len(s) - i):
        if not s[j:j+i] in d:
            d[s[j:j+i]] = ''
print(len(d))
