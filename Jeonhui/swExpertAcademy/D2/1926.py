n = int(input())
for i in range(1, n + 1):
    cnt = 0
    for x in str(i):
        if x == '3' or x == '6' or x == '9':
            cnt += 1
    print(('-' * cnt) if cnt != 0 else i, end=" ")
