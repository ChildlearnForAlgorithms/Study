import sys
a= sys.stdin.readline().split()
print(a[0][::-1] if int(a[0][::-1]) > int(a[1][::-1]) else a[1][::-1])