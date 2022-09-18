import time, random


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def compute_e_ver1(n):
    sum = 1
    for i in range(1, n + 1):
        f = factorial(i)
        sum += 1 / f
    return sum


# code for O(n^2)-time version

def compute_e_ver2(n):
    sum = 1
    for i in range(2, n + 1):
        f = factorial(i - 1) * i
        sum += 1 / f
    return sum


# code for O(n)-time version

n = random.randint(100, 500000)  # 실험할 때는 n=int(input())으로 입력 받아 실험했음

before1 = time.process_time()
compute_e_ver1(n)
# compute_e_ver1 호출
after1 = time.process_time()

before2 = time.process_time()
compute_e_ver2(n)
# compute_e_ver2 호출
after2 = time.process_time()

print(after1 - before1)
print(after2 - before2)
# 두 함수의 수행시간 출력
