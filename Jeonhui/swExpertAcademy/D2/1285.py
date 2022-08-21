T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    minD,cnt = 100000,0
    for x in list(map(int, input().split())):
        if minD > abs(x):
            minD,cnt = abs(x),1
        elif minD == abs(x):
            cnt += 1
    print(f"#{test_case} {minD} {cnt}")
