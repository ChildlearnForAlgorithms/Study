T = int(input())
for test_case in range(1, T + 1):
    na, nb = map(int, input().split())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    if na > nb:
        na, nb = nb, na
        a, b = b, a
    maxRes, res = 0, 0
    for i in range(nb - na + 1):
        res = 0
        for j in range(na):
            res += a[j] * b[i + j]
        print(res)
        if maxRes < res:
            maxRes = res
    print(f"#{test_case} {maxRes}")
