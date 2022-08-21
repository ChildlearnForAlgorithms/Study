T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    max = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sum = 0
            for x in range(i, i + m):
                for y in range(j, j + m):
                    sum += A[x][y]
            if max < sum:
                max = sum
    print(f"#{test_case} {max}")
