T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    A=[input().split() for i in range(n)]
    res90 = [list(reversed([A[i][j] for i in range(n)])) for j in range(n)]
    res180 = [list(reversed([res90[i][j] for i in range(n)])) for j in range(n)]
    res270 = [list(reversed([res180[i][j] for i in range(n)])) for j in range(n)]
    print(f"#{test_case}")
    for i in range(n):
        print(f"{''.join(res90[i])} {''.join(res180[i])} {''.join(res270[i])}")