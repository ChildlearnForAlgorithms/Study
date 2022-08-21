T = int(input())
for test_case in range(1, T + 1):
    l = sorted(list(map(int, input().split())))
    print(f"#{test_case} {l[len(l) // 2]}")
