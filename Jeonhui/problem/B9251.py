import sys


def LIS(A, B):
    DP = [[0] * (len(A) + 1) for i in range(len(B) + 1)]
    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):

            if A[j - 1] != B[i - 1]:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
            else:
                DP[i][j] = DP[i - 1][j - 1] + 1
    for i in range(len(DP)):
        print(DP[i])
    return DP[len(B)][len(A)]


a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
'''
a = "ACAYKP"
b = "CAPCAK"'''
print(LIS(a, b))
