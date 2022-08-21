T = int(input())
thirty = [4, 6, 9, 11]
thirtyOne = [1, 3, 5, 7, 8, 10, 12]
for test_case in range(1, T + 1):
    d = input()
    print(f"#{test_case} {(d[:4] + '/' + d[4:6] + '/' + d[6:8]) if (xint(d[4:6]) == 2 and 0 < int(d[6:8]) <= 28) or (int(d[4:6]) in thirty and 0 < int(d[6:8]) <= 30) or (int(d[4:6]) in thirtyOne and 0 < int(d[6:8]) <= 31) else '-1'}")
