n = int(input())
lst = []

for i in range(n):
    color = list(map(int, input().split()))
    lst.append(color)
dp = [[0] * 3 for _ in range(n)]

for i in range(3):
    dp[0][i] = lst[0][i]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + lst[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + lst[i][j]
        elif j == 2:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + lst[i][j]

answer = [0] * 3

for i in range(3):
    answer[i] = dp[n - 1][i]

print(min(answer))
