n = int(input())
p = n // 5

def cut(n, p):
    count = 0
    if p < 0:
        return count
    elif n==4 or n==7:
        return -1
    elif p>=0:
        if (n-p*5) % 3 == 0:
            count += p + ((n-p*5) // 3)
            return count
        elif (n % 5) % 3 != 0:
            return cut(n,p-1)
    else:
        return -1


print(cut(n,p))
