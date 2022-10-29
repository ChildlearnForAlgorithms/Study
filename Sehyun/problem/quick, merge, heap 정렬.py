import random, timeit


##
## 여기에 세 가지 정렬함수를 위한 코드를...
##

def quick_sort(A, first, last):
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

#추가 점수 1:

def quick_insertion_sort(A, first, last): #분할한 구간의 크기가 k(10과 40 사이의 상수) 이하가 되면 insertion_sort로 정렬하는 quick_sort
	global Qc, Qs #글로벌 변수 선언
	if last - first + 1 <= random.randint(10, 40):
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
	
#추가 점수 2:

def quick_sort_after_insertion(A, first, last):
    global Qc, Qs  # 글로벌 변수 선언
    if last - first + 1 <= random.randint(10, 40):
        insertion_sort(A, first, last)
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
    quick_sort_after_insertion(A, first, right - 1)  # S 정렬
    quick_sort_after_insertion(A, left, last)  # L 정렬

def insertion_sort(A, first, last):
	for i in range(first, last+1):
		j = i - 1
		while j >= 0 and A[j] > A[j + 1]: 
			A[j], A[j + 1] = A[j + 1], A[j]
			j = j - 1

			
#추가 점수 3:

def merge(A, i, j, k, l):
    # i <= j and j < k <= l
    # 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수
    B = []
    x, y = i, k
    while x <= j and y <= l:
        if A[x] <= A[y]:
            B.append(A[x])
            x += 1
        else:
            B.append(A[y])
            y += 1
    for a in range(x, j + 1): B.append(A[a])
    for b in range(y, l + 1): B.append(A[b])
    for c in range(i, l + 1): A[c] = B[c - i]


def m_sort(A, first, last):
    # 3-way merge sort - merge 함수를 이용해 적절히 합병한다
    if first >= last: return
    trip = (last - first) // 3
    m_sort(A, first, first + trip)
    m_sort(A, first + trip + 1, first + 2 * trip)
    m_sort(A, first + 2 * trip + 1, last)

    merge(A, first, first + trip, first + trip + 1, first + 2 * trip)
    merge(A, first, first + 2 * trip,
          first + 2 * trip + 1, last)




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
'''
print("quick_insertion_sort:")
print("time =", timeit.timeit("quick_insertion_sort(A, 0, n-1)", globals=globals(), number=1))

print("quick_sort_after_insertion:")
print("time =", timeit.timeit("quick_sort_after_insertion(A, 0, n-1)", globals=globals(), number=1))

print("m_sort:")
print("time =", timeit.timeit("m_sort(A, 0, n-1)", globals=globals(), number=1))

일반적인 quick sort랑 k개 이하로 분할한 후 분할한 것들을 insertion sort한 것과
k개 이하로 분할한 후 전체를 대상으로 insertion sort한 것을 비교해보았을 때 일반적인
quick sort가 훨씬 빨랐다. 그리고 2-way merge sort와 3-way merge sort를 비교해봤을 땐
3-way merge sort가 조금 더 빨랐다.'''


# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert (check_sorted(A))
assert (check_sorted(B))
assert (check_sorted(C))