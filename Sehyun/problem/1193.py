n = int(input())
a = 1
i = 2
if n == 1:
    print('1/1')
while n > a:
    a += i
    i += 1
    if n <= a:
        d = a - n
        if (i-1) % 2 == 0:
            x = i - 1 - d
            y = i - x
            print("%d/%d" % (x, y))
            break
        elif (i-1) % 2 == 1:
            x = i - 1 - d
            y = i - x
            print("%d/%d" % (y, x))
            break
