T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    idx, mod = 1, 0
    A = [[0 for _ in range(n)] for _ in range(n)]
    a, b, x, y, w, z = 0, 0, 0, n - 1, 0, n - 1
    for i in range(1, n * n + 1):
        A[a][b] = i
        if mod == 0:  # 오른쪽
            if b == y:
                mod = (mod + 1) % 4
                w, a = w + 1, a + 1
            else:
                b += 1
        elif mod == 1:  # 아래
            if a == z:
                mod = (mod + 1) % 4
                y, b = y - 1, b - 1
            else:
                a += 1
        elif mod == 2:  # 왼쪽
            if b == x:
                mod = (mod + 1) % 4
                z, a = z - 1, a - 1
            else:
                b -= 1
        else:
            if a == w:
                mod = (mod + 1) % 4
                x, b = x + 1, b + 1
            else:
                a -= 1
    print(f"#{test_case}")
    for i in range(n):
        print(" ".join(list(map(str, A[i]))))
