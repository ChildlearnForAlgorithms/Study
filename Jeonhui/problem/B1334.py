import sys

# num = sys.stdin.readline().rstrip()
# x = num[:(len(num) + 1) // 2]
# res = 0
# if len(num) % 2 == 1:
#     res = x + "".join(reversed(x[:-1]))
#     while int(res) <= int(num):
#         x = str(int(x) + 1)
#         res = x + "".join(reversed(x[:-1]))
#         if len(res) > len(num):
#             res = "1" + "0" * (len(num) - 1) + "1"
# else:
#     res = x + "".join(reversed(x))
#     while int(res) <= int(num):
#         x = str(int(x) + 1)
#         res = x + "".join(reversed(x))
#         if len(res) > len(num):
#             res = "1" + "0" * (len(num) - 1) + "1"
# print(res)

import sys


def Palindrom(words):
    for i in range(len(words) // 2):
        if words[i] != words[len(words) - 1 - i]:
            return False
    return True


n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    state = 0
    word = []
    for _ in range(k):
        res = []
        word.append(sys.stdin.readline().rstrip())
    for i in range(k):
        for j in range(k):
            if i != j and Palindrom(word[i] + word[j]):
                state = 1
                print(word[i] + word[j])
                break
        if state == 1:
            break
    if state == 0:
        print(0)
