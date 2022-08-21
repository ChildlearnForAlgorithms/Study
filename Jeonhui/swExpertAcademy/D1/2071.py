T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {sum([num for num in list(map(int, input().split()))])/10:.0f}")