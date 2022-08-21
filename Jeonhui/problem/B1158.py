def yose(n, k):
    A = [i for i in range(1, n + 1)]
    B = []
    x = 0
    for i in range(n):
        x = (x + k - 1) % len(A)
        B.append(str(A.pop(x)))
    return "<" + ", ".join(B) + ">"

n, k = map(int, input().split())
print(yose(n, k))

'''
def yose(n, k):
    A = [i for i in range(1, n + 1)]
    B = []
    x = 0
    for i in range(n):
        x = (x + k - 1)%len(A)
        B.append(A.pop(x))
    print(B)


yose(7, 3)
'''
