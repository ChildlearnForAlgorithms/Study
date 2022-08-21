from datetime import datetime
d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
T = int(input())
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    t1, t2 = datetime(2022, m1, d1), datetime(2022, m2, d2)
    diff = t2 - t1
    print(f"#{test_case} {diff.days+1}")