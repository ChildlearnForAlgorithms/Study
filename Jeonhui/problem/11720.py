import sys

n = int(sys.stdin.readline())
print([int(i) for i in sys.stdin.readline().rstrip()])
print(sum([int(i) for i in sys.stdin.readline().rstrip()]))

'''
n = int(input())
print(sum([int(i) for i in input()]))
'''