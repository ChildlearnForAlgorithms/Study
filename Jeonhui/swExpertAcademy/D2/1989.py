T = int(input())
for test_case in range(1, T + 1):
    string = input().rstrip()
    answer, n = 1, len(string) - 1
    for i in range(len(string) // 2):
        if string[i] != string[n - i]:
            answer = 0
            break
    print(f"#{test_case} {answer}")
