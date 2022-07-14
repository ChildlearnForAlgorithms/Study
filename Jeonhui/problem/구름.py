def max_sum(A, left, right):
    if left==right:
        return A[left]
    mid = (left + right) // 2
    l=max_sum(A,left,mid)
    r=max_sum(A,mid+1,right)
    sum1=0
    sum2=0
    l2=-1000
    r2=-1000
    for i in range(mid,left-1,-1):
        sum1+=A[i]
        l2=max(l2,sum1)
    for i in range(mid,right+1,1):
        sum2+=A[i]
        r2=max(r2,sum2)
    return max(l,r,l2+r2)
A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A) - 1)
print(sol)
