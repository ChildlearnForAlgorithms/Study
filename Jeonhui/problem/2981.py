import sys
import math

n = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
result = []

gcdValue = nums[1] - nums[0]

for i in range(2, len(nums)):
    gcdValue = math.gcd(gcdValue, nums[i] - nums[i - 1])
for m in range(2, gcdValue//2 + 1):
    if gcdValue % m == 0:
        result.append(m)
result.append(gcdValue)

print(" ".join(list(map(str, result))))