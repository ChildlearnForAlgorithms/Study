import sys


def check(A, n):
    stack = []
    res = [0] * n
    exp = []
    k = 0
    for x in range(1, n + 1):
        exp.append("+")
        stack.append(x)
        while len(stack) > 0:
            if A[k] != stack[-1]:
                break
            if stack[-1] == A[k]:
                res[k] = stack.pop()
                exp.append("-")
                k += 1
    if len(stack) > 0:
        return ["NO"]
    return exp


n = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(n)]
exp = check(A, n)
for i in range(len(exp)):
    print(exp[i])
