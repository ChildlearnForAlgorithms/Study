T = int(input())
for test_case in range(1, T + 1):
    A = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    dx, dy, dz = {}, {}, {}
    x, y = 0, 0
    for i in range(9):
        for j in range(9):
            dx[A[i][j]], dy[A[j][i]] = '', ''
            dz[A[x + (j // 3)][y + (j % 3)]] = ''
        if answer == 0 or len(dx.keys()) != 9 or len(dy.keys()) != 9 or len(dz.keys()) != 9:
            answer = 0
            break
        dx, dy, dz = {}, {}, {}
        y += 3
        if y == 9:
            x, y = x + 3, 0
    print(f"#{test_case} {answer}")
