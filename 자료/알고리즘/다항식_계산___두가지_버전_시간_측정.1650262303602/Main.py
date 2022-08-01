import time, random


# O(n^2)을 가지는 다항식 계산
def evaluate_n2(A, x):
    res = 0
    for i in range(len(A)):
        Xn = 1
        for _ in range(i):
            Xn *= x
        res = A[i] * Xn + res
    return res


# O(n)을 가지는 다항식 계산
def evaluate_n(A, x):
    res = 0
    Xn = 1
    for i in range(len(A)):
        res = A[i] * Xn + res
        Xn = Xn * x
    return res


random.seed()  # random 함수 초기화
n = int(input())  # n 입력받음
A = [random.randint(-1000, 1000) for _ in range(n)]  # 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움

x = random.randint(-1000, 1000)
s1 = time.process_time()
evaluate_n2(A, x)  # evaluate_n2 호출
e1 = time.process_time()

s2 = time.process_time()
evaluate_n(A, x)  # evaluate_n 호출
e2 = time.process_time()

print("O(n^2) 수행시간 = ", e1 - s1)
print("O(n) 수행시간 = ", e2 - s2)
# 두 함수의 수행시간 출력
