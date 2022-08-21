T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, T + 1):
    n, res = int(input()),[]
    for m in money:
        res.append(str(n//m))
        n %= m
    print(f"#{test_case}\n"+" ".join(res))