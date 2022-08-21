T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print(f"#{test_case} {' '.join(map(str,sorted(list(map(int,input().split())))))}")