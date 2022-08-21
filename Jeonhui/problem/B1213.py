import sys

d = {}
words = sys.stdin.readline().rstrip()

for i in range(len(words)):
    if words[i] not in d:
        d[words[i]] = 0
    d[words[i]] += 1

key = sorted(d.keys())
cnt_Odd = 0
res = ""

for k in key:
    res += k * (d[k] // 2)
    if d[k] % 2 == 1:
        d[k] = 1
    else:
        d.pop(k)
if len(d) > 1:
    res = "I'm Sorry Hansoo"
else:
    res = res + (list(d.keys())[0] if len(d) == 1 else "") + "".join(reversed(res))
print(res)
