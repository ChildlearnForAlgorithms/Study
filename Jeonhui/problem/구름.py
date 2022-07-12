def max_sum(A):
    # 최대 구간 합 리턴
    n = len(A)
    P = [0 for _ in range(n)]
    P[0] = A[0]
    for i in range(1, n):
        P[i] = P[i - 1] + A[i]
    max_partial_sum = P[0]

    for b in range(n):
        for a in range(b):
            if max_partial_sum < P[b] - P[a]:
                max_partial_sum = P[b] - P[a]
            print(f"b {b} ~ a {a}, {max_partial_sum}")
    return max_partial_sum


A = [int(x) for x in input().split()]
sol = max_sum(A)
print(sol)
