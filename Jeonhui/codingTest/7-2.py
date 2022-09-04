import sys

n = int(sys.stdin.readline())
parts = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
findParts = list(map(int,sys.stdin.readline().split()))

result = []

parts.sort()
for findPart in findParts:
    start = 0
    end = len(parts) - 1
    isExist = False
    while start <= end:
        mid = (start + end) // 2
        if parts[mid] > findPart:
            end = mid - 1
        elif parts[mid] < findPart :
            start = mid + 1
        else:
            isExist = True
            break
    result.append("yes" if isExist else "no")
print(" ".join(result))
