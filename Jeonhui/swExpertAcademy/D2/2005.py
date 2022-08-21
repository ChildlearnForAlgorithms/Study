T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    A = []
    for i in range(n):
        A.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                A[i].append(1)
            else:
                A[i].append(A[i-1][j-1]+A[i-1][j])
    print(f"#{test_case}")
    for i in range(n):
        print(" ".join(map(str,A[i])))