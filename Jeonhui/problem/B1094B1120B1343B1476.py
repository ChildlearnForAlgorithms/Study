#B1094
# import sys
# print(sum(map(int, str(bin(int(sys.stdin.readline())))[2:])))

#B1120
# import sys
#
# a, b = map(str, sys.stdin.readline().split())
# res = 50
# for i in range(len(b) - len(a) + 1):
#     c = b[i:i+len(a)]
#     cnt = 0
#     for j in range(len(a)):
#         if c[j] != a[j]:
#             cnt += 1
#     if res > cnt:
#         res = cnt
# print(res)

#B1343
# import sys
# 폴리노미오
# p = sys.stdin.readline().rstrip().split(".")
# for i in range(len(p)):
#     if len(p[i]) % 2 == 1:
#         p = ["-1"]
#         break
#     elif p[i] != "":
#         p[i] = ("AAAA" * (len(p[i]) // 4)) + ("BB" * ((len(p[i]) % 4) // 2))
# print(".".join(p))

#B1476
import sys

e, s, m = map(int, sys.stdin.readline().split())
a, b, c = 1, 1, 1
year = 1
while a != e or s != b or m != c:
    year += 1
    a = a % 15 + 1
    b = b % 28 + 1
    c = c % 19 + 1
print(year)
