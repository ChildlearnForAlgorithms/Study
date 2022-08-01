n = int(input())
A = list(map(int, input().split()))


def max_interval_DP(A):
    S = [0] * len(A)
    S[0] = A[0]
    for i in range(1, len(A)):
        S[i] = max(S[i - 1] + A[i], A[i])
    return S.index(max(S))


print(max_interval_DP(A))
