T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = W*P
    B = Q if W<R else (Q + (W-R)*S)
    print(f"#{test_case} {B if A>B else A}")
