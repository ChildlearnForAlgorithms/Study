import random, timeit


##
## 여기에 세 가지 정렬함수를 위한 코드를...
##

def quick_sort(A, first, last):  # in-place quick sort
    global Qc, Qs  # 글로벌 변수 선언
    if first >= last:
        return
    left, right = first + 1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
            Qc += 1  # while문이 한번 돌때마다 비교횟수 1번 늘어나므로
        while A[right] > pivot:
            right -= 1
            Qc += 1  # while문이 한번 돌때마다 비교횟수 1번 늘어나므로
        if left <= right:
            A[left], A[right] = A[right], A[left]  # 교환
            left += 1
            right -= 1
            Qs += 1  # 교환횟수+1
    A[right], A[first] = A[first], A[right]
    Qs += 1  # 교환횟수+1
    quick_sort(A, first, right - 1)  # S 정렬
    quick_sort(A, left, last)  # L 정렬


"""
def quick_insertion_sort(A, first, last): #나눈 구간의 크기가 k(10) 이하가 되면 insertion_sort로 정렬하는 quick_sort
	global Qc, Qs #글로벌 변수 선언
	if last - first + 1 <= 10:
		for end in range(first+1,last+1):
			for i in range(end,first,-1):
				Qc += 1
				if A[i] < A[i-1]:
					A[i-1], A[i] = A[i], A[i-1]
					Qs += 1
				else:
					break
		return
	p = A[first]
	left, right = first+1, last
	while left <= right:
		while left <= last and A[left] < p:
			left += 1
			Qc += 1 #while문이 한번 돌때마다 비교횟수 1번 늘어나므로
		while A[right] > p:
			right -= 1
			Qc += 1 #while문이 한번 돌때마다 비교횟수 1번 늘어나므로
		if left <= right:
			A[left], A[right] = A[right], A[left] #교환
			left += 1
			right -= 1
			Qs += 1 #교환횟수+1
	A[right], A[first] = A[first], A[right]
	Qs += 1 #교환횟수+1
	quick_insertion_sort(A,first,right-1) #S 정렬
	quick_insertion_sort(A,left,last) #L 정렬
"""


def merge_sort(A, first, last):
    global Mc, Ms  # 비교, 교환횟수 글로벌 변수로
    if first >= last: return  # 종료조건
    m = (first + last) // 2  # 절반으로 나눔
    merge_sort(A, first, m)  # 앞 부분 재귀
    merge_sort(A, m + 1, last)  # 뒷 부분 재귀
    i, j = first, m + 1  # 탐색 인덱스 설정
    B = []
    while i <= m and j <= last:  # 정렬된 두 부분을 오름차순으로 B에 저장
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
        Mc += 1
        Ms += 1
    for k in range(i, m + 1):  # 앞 절반 중 남은 부분이 있으면 B에 저장
        B.append(A[k])
        Ms += 1
    for k in range(j, last + 1):  # 뒤 절반 중 남은 부분이 있으면 B에 저장
        B.append(A[k])
        Ms += 1
    for k in range(first, last + 1):  # B에 정렬된 순서대로 A에 저장
        A[k] = B[k - first]
        Ms += 1


"""
def merge_insertion_sort(A, first, last): #나눈 구간의 크기가 k(10) 이하가 되면 insertion sort를 사용하는 merge sort
	global Mc, Ms #비교, 교환횟수 글로벌 변수로
	if last - first + 1 <= 10:
		for end in range(first+1,last+1):
			for i in range(end,first,-1):
				Mc += 1
				if A[i] < A[i-1]:
					A[i-1], A[i] = A[i], A[i-1]
					Ms += 1
				else:
					break
		return
	m = (first+last)//2 #절반으로 나눔
	merge_insertion_sort(A, first, m) #앞 부분 재귀
	merge_insertion_sort(A, m+1, last) #뒷 부분 재귀
	i, j = first, m+1 #탐색 인덱스 설정
	B = []
	while i<=m and j<=last: #정렬된 두 부분을 오름차순으로 B에 저장
		if A[i] <= A[j]:
			B.append(A[i])
			i += 1
		else:
			B.append(A[j])
			j += 1
		Mc += 1
		Ms += 1
	for k in range(i,m+1): #앞 절반 중 남은 부분이 있으면 B에 저장
		B.append(A[k])
		Ms += 1
	for k in range(j,last+1): #뒤 절반 중 남은 부분이 있으면 B에 저장
		B.append(A[k])
		Ms += 1
	for k in range(first, last+1): #B에 정렬된 순서대로 A에 저장
		A[k] = B[k-first]
		Ms += 1
"""


def heapify_down(A, k, n):  # max heap
    global Hc, Hs
    while 2 * k + 1 <= n - 1 or 2 * k + 2 <= n - 1:
        L, R = 2 * k + 1, 2 * k + 2
        if 2 * k + 2 > n - 1:
            R = L
        if A[L] > A[R]:
            m = L
        else:
            m = R
        Hc += 1
        if A[k] < A[m]:
            A[k], A[m] = A[m], A[k]
            k = m
            Hc += 1
            Hs += 1
        else:
            Hc += 1
            break


def make_heap(A):  # max heap 만드는 함수
    n = len(A)
    for k in range(n - 1, -1, -1):
        heapify_down(A, k, n)


def heap_sort(A):
    global Hc, Hs
    make_heap(A)  # A를 max heap으로 만듦
    n = len(A)
    for i in range(n - 1, -1, -1):  # 루트를 계속 A의 맨 뒤의 요소와 교환하고 heap의 범위를 1씩 줄이면 오름차순으로 정렬됨
        A[0], A[i] = A[i], A[0]
        Hs += 1
        heapify_down(A, 0, i)


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
    for i in range(n - 1):
        if A[i] > A[i + 1]: return False
    return True


#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert (check_sorted(A))
assert (check_sorted(B))
assert (check_sorted(C))