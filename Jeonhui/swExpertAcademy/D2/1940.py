T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    speed, distance = 0, 0
    for i in range(n):
        command = list(map(int, input().split()))
        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            speed -= command[1]
            if speed < 0:
                speed = 0
        distance += speed
    print(f"#{test_case} {distance}")
