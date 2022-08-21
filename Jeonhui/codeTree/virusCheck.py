import sys

n = int(sys.stdin.readline())  # 식당 수
cons = list(map(int, sys.stdin.readline().split()))
TLMaxCons, TMMaxCons = map(int, sys.stdin.readline().split())
T = []
for i in range(len(cons)):
    A = (((cons[i] - TLMaxCons) // TMMaxCons + 1) if (cons[i] - TLMaxCons) % TMMaxCons != 0 else (cons[i] - TLMaxCons) // TMMaxCons) + 1
    T.append(A)
print(sum(T))
