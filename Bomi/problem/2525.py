start_H, start_M = map(int,input().split())
cooking_time = int(input())

hour = (start_M + cooking_time) // 60
start_M = (start_M + cooking_time) % 60

if hour > 0:
	if (start_H + hour) >= 24:
		start_H = (start_H + hour) - 24
	else:
		start_H += hour

print(start_H, start_M)