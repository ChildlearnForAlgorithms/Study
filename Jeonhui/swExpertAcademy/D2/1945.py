T = int(input())
primes = [2, 3, 5, 7, 11]
for test_case in range(1, T + 1):
    n = int(input())
    res = [0, 0, 0, 0, 0]
    for i in range(len(primes)):
        while n % primes[i] == 0:
            n //= primes[i]
            res[i] += 1
    print(f"#{test_case} {' '.join(list(map(str, res)))}")