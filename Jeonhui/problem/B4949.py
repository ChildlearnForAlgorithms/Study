import sys


def check(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append("(")
        elif c == "[":
            stack.append("[")
        elif c == ")":
            if len(stack) < 1 or stack.pop() != "(":
                return False
        elif c == "]":
            if len(stack) < 1 or stack.pop() != "[":
                return False
    if len(stack) > 0:
        return False
    else:
        return True


s = ""
while True:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    print("yes" if check(s) else "no")
