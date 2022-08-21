import sys

n = int(sys.stdin.readline())
current_hw = []
score = 0
for i in range(n):
    time = list(map(int, sys.stdin.readline().split()))
    if time[0] == 1:
        current_hw.append([time[1], time[2]])
    if len(current_hw) > 0:
        current_hw[-1][1] -= 1
        if current_hw[-1][1] == 0:
            score += current_hw[-1][0]
            current_hw.pop()
print(score)
