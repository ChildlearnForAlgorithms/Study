import sys

n,m=map(int,sys.stdin.readline().split())
nums=[]

def print_permutation():
    for elem in nums:
        print(elem,end=' ')
    print()

def find_permutation(start):
    if len(nums)==m:
        print_permutation()
        return
    for i in range(start,n+1):
        nums.append(i)
        find_permutation(i)
        nums.pop()

find_permutation(1)