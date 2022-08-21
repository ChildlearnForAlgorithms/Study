T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        x,y = 0,0
        for j in range(n):
            if A[i][j] == 1:
                x += 1
            if A[i][j] == 0 or j == n - 1:
                if x == k: cnt += 1
                x = 0
            if A[j][i] == 1:
                y += 1
            if A[j][i] == 0 or j == n - 1:
                if y == k: cnt += 1
                y = 0
    print(f"#{test_case} {cnt}")
