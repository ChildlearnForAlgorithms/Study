T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {round(sum(sorted(list(map(int, input().split())))[1:9])/8)}")