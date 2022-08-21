# 11650
'''
import sys
n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lst.sort()
for i in range(n):
    print(lst[i][0], lst[i][1])
'''

# 11651
'''
import sys
n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lst = sorted(lst, key= lambda x:(x[1],x[0]))
for i in range(n):
    print(lst[i][0], lst[i][1])
'''

# 1181
'''
import sys

n = int(sys.stdin.readline())
lst = [sys.stdin.readline().rstrip() for _ in range(n)]
for c in sorted(list(set(lst)), key=lambda x: (len(x),x)):
    print(c)
'''
# 10814
'''
import sys

n = int(sys.stdin.readline())
lst = [sys.stdin.readline().split() for _ in range(n)]
for p in sorted(lst, key=lambda x: int(x[0])):
    print(p[0], p[1])
'''
# 18870
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
seq = sorted(set(lst))
d={}
for i in range(len(seq)):
    d[seq[i]] = i
for i in lst:
    print(d[i],end=" ")