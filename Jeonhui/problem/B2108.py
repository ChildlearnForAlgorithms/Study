import sys
from collections import Counter

n = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for i in range(n)]
A.sort()
cnt = Counter(A).most_common(2)
print(int(round(sum(A) / n, 0)))
print(A[n // 2])
print(cnt[1][0] if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0])
print(abs(A[-1] - A[0]))
