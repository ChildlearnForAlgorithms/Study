import sys

s = sys.stdin.readline().rstrip()
tmp = ""
res = 0
state = False

for c in s:
    if c == "+" or c == "-":
        res += (-int(tmp) if state else int(tmp))
        tmp = ""
        if c=="-":
            state = True
    else:
        tmp += c
res += (-int(tmp) if state else int(tmp))
print(res)
