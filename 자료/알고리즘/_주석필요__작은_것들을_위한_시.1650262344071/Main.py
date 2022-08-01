def minSum(A):
	S = [0] * len(A)
	S[0] = A[0]
	for k in range(1, len(A)):
		if A[k - 1] < A[k]:
			S[k] = S[k - 1] + A[k]
		else:
			m = k - 1
			while A[k] < A[m] and m != -1:
				m -= 1
			S[k] = S[m] + A[k] * (k - m)
	return sum(S)


A=list(map(int, input().split()))
print(minSum(A))

'''
DP테이블은 n만큼의 크기를 가지고
k번째 수까지의 부분배열들의 최소값들을 저장한다.
A[k]와 A[k - 1]를 비교하여 A[k]가 더 클 경우
S[k] = S[k - 1] + A[k] 이고,
작을 경우, A[m]이 A[k]보다 작은 가장 가까운 수일 때
S[k] = S[m] + A[k] * (k - m) 이다.
수행시간은 최상의 경우 오름차순으로 입력이 들어왔을 때이다.
이 경우에는 O(n)의 수행시간을 가진다.
반대로 최악의 경우는 내림차순으로 입력이 들어왔을 때이고,
이 경우에는 수행시간이 O(n^2)이 나온다.
하지만 while문에서 수행하는 연산이 m -= 1뿐이므로
평균 수행시간의 경우 O(n^2)보다 훨씬 빠르게 작동한다.
'''