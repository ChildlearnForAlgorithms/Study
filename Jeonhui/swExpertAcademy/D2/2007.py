T = int(input())
for test_case in range(1, T + 1):
    A = input()
    answer = 0
    for i in range(1, 31):
        for j in range(0, 30, i):
            if A[:i] == A[i: i * 2]:
                answer = i
                break
            else:
                continue
        if answer != 0:
            break

    print(f"#{test_case} {answer}")
