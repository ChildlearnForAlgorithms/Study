n,m=map(int,input().split())
nums=[]
def print_permutation():
    for num in nums:
        print(num,end=' ')
    print()

def find_permutation(cnt):
    if cnt==m:
        print_permutation()
        return
    for i in range(1,n+1):
        nums.append(i)
        find_permutation(cnt+1)
        nums.pop()

find_permutation(0)
