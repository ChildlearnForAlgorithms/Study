import sys,heapq

A=list(map(int,sys.stdin.readline().split()))
n=len(A)
m=[]

def check(A):
    global i
    while i<n:
        small, big = [], []
        result = []
        k=i//3+1
        for elem in A[:i+1]:
            if not small or -small[0]>=elem:
                heapq.heappush(small,-elem)
            else:
                heapq.heappush(big,elem)

            if len(small)>k:
                heapq.heappush(big,-heapq.heappop(small))
            elif len(small)<k and big:
                heapq.heappush(small,-heapq.heappop(big))

            result.append(-small[0] if len(small)>=k else -1)
        i+=1
        m.append(result[-1])



i=0
check(A)
print(sum(m))