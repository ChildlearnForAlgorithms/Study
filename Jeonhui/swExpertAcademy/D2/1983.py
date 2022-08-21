T = int(input())
gpa = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    A = []
    kg = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        g = a * 0.35 + b * 0.45 + c * 0.2
        A.append(g)
        if i == k-1:
            kg = g
    A.sort(key=lambda x:-x)
    for i in range(n):
        if A[i] == kg:
            print(f"#{test_case} {gpa[i//(n//10)]}")
            break

