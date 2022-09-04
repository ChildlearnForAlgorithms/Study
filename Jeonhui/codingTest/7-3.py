import sys

n, m = map(int, sys.stdin.readline().split())
tteok = list(map(int, sys.stdin.readline().split()))

result = 0
start = 0
end = max(tteok)

while start <= end:
    mid = (start + end) // 2
    total = sum([t - mid for t in tteok if t - mid > 0])
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
