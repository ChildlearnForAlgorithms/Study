class Heap:
    def __init__(self, L=[]):
        self.A=L
        self.make_heap()

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):
        while 2*k+1<n:
            left,right=2*k+1,2*k+2
            if left<n and self.A[left]>self.A[k]:
                m=left
            else:
                m=k
            if right<n and self.A[right]>self.A[m]:
                m=right
            if m!=k:
                self.A[m],self.A[k]=self.A[k],self.A[m]
                k=m
            else:
                break




    def make_heap(self,):
        n=len(self.A)
        for i in range(n-1,-1,-1):
            self.heapify_down(i,n)

    def heap_sort(self):
        n=len(L)
        for i in range(n-1,-1,-1):
            self.A[0],self.A[i]=self.A[i],self.A[0]
            n=n-1
            self.heapify_down(0,n)




L = [int(x) for x in input().split()]
H = Heap(L)
H.heap_sort()
print(H)
