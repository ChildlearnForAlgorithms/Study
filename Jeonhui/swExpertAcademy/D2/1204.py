T = int(input())
for test_case in range(1, T + 1):
    x = int(input())
    A = [0]*101
    maxI = 0
    for score in list(map(int, input().split())):
        A[score] += 1
        if A[score] >= A[maxI]:
            maxI = score
    print(f"#{x} {maxI}")
