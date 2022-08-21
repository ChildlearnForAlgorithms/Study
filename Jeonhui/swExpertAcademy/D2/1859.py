T = int(input())
for test_case in range(1, T + 1):
    sum = 0
    maxNum = 0
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N - 1, -1, -1):
        if maxNum < A[i]:
            maxNum = A[i]
        sum += (maxNum - A[i])
    print(f"#{test_case} {sum}")
