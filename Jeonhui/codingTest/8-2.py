'''
정수 X가 주어졌을 때, 다음 조건의 연산 4개를 사용하여 1을 만든다. 이때 연산을 사용하는 횟수의 최솟값을 출력한다.

- X가 5로 나누어떨어지면, 5로 나눈다.
- X가 3으로 나누어떨어지면, 3으로 나눈다.
- X가 2로 나누어떨어지면, 2로 나눈다.
- X에서 1을 뺀다.
'''

import sys

x = int(sys.stdin.readline())
d = [0] * (x + 1)

for i in range(x, 0, -1):
    for n in [2, 3, 5]:
        if i % n == 0:
            d[i // n] = min(d[i] + 1, d[i // n]) if d[i // n] != 0 else d[i] + 1
        d[i - 1] = min(d[i] + 1, d[i - 1]) if d[i - 1] != 0 else d[i] + 1
print(d)
