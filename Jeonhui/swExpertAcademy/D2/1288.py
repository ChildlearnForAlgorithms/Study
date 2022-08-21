T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    d,x = {},n
    while True:
        for i in str(x):
            d[i] = 1
        if len(d.keys()) >= 10:
            break
        x += n
    print(f"#{test_case} {x}")
