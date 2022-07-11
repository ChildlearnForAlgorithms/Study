def find_median_five(A):
	n = len(A)
	# n//2번 반복 n=1:0,n=2:1,n=3:1,n=4:2,n=5:2
	# 없애야하는 max개수
	for _ in range(n // 2):
		maxI = 0
		# 최대 값의 인덱스를 찾는 문장
		for i in range(1, len(A)):
			if A[maxI] < A[i]:
				maxI = i
				# A에서 최대 값을 제외함
		A = A[:maxI] + A[maxI + 1:]
		# n//2개의 max값을 제외한 나머지 중 가장 큰 값
	return max(A)

'''
def median(A):
    n=len(A)
    for i in range(n//2):
        maxI=A.index(max(A))
        A=A[:maxI]+A[maxI+1:]
    return max(A)
'''

def MoM(A, k):  # L의 값 중에서 k번째로 작은 수 리턴
    if len(A) == 1:  # no more recursion
        return A[0]
    i = 0
    S, M, L, medians = [], [], [], []
    while i + 4 < len(A):
        medians.append(find_median_five(A[i: i + 5]))
        i += 5

    if i < len(A) and i + 4 >= len(A):  # 마지막 그룹으로 5개 미만의 값으로 구성
        medians.append(find_median_five(A[i:]))

    mom = MoM(medians, len(medians) // 2)
    for v in A:
        if v < mom:
            S.append(v)
        elif v > mom:
            L.append(v)
        else:
            M.append(v)

    if len(S) >= k:
        return MoM(S, k)
    elif len(S) + len(M) < k:
        return MoM(L, k - len(S) - len(M))
    else:
        return mom


n, k = map(int, input().split())
# n과 k를 입력의 첫 줄에서 읽어들인다
A = list(map(int, input().split()))
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
print(MoM(A, k))

