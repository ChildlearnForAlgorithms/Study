def m_sort(A, first, last):
    if first>=last:
        return
    m1=(first+last)//3
    m2=(first+last)*2//3
    m_sort(A,first,m1)
    m_sort(A, m1+1, m2)
    m_sort(A, m2 + 1, last)
    merge(A, first, m1, m2, last)

def merge(A, first, m1, m2, last):
    i=first
    j=m1+1
    k=m2+1
    B=[]
    while i<=m1 and j<=m2 and k<=last:
        if A[i]<=A[j]:
            if A[i]<=A[k]:
                B.append(A[i])
                i+=1
            else:
                B.append(A[k])
                k+=1
        else:
            if A[j]<=A[k]:
                B.append(A[j])
                j+=1
            else:
                B.append(A[k])
                k+=1
    while j <= m2 and k<=last:
        if A[j]<=A[k]:
            B.append(A[j])
        else:
            B.append(A[k])
    while i <= m1 and k<=last:
        if A[i]<=A[k]:
            B.append(A[i])
        else:
            B.append(A[k])
    while i <= m1 and j <= m2:
        if A[i]<=A[j]:
            B.append(A[i])
        else:
            B.append(A[j])

    while i<=m1:
        B.append(A[i])
    while j<=m2:
        B.append(A[j])
    while k<=last:
        B.append(A[k])
    for i in range(first,last+1):
        A[i]=B[i-first]

def check(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return A[0]+A[(len(A)//2)]+A[-1]

A = [int(x) for x in input().split()]
m_sort(A, 0, len(A)-1)
print(check(A))

