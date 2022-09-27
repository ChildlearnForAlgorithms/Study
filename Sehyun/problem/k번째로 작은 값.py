import sys,heapq

A=list(map(int,sys.stdin.readline().split()))
n=len(A)
def check(A,k):
    small,big=[],[]
    result=[]
    for i in A:
        if not small or -small[0]>=i:
            heapq.heappush(small,-i)
        else:
            heapq.heappush(big,i)

        if len(small)>k:
            heapq.heappush(big,-heapq.heappop(small))
        elif len(small)<k and big:
            heapq.heappush(small,-heapq.heappop(big))

        result.append(-small[0] if len(small)>=k else -1)

    return result

print(sum)