def solve(A):
	n = len(A)
	m = max(A)
	
	S = [[0] * m for _ in range(n)]
	#[최대값]*배열의 수
	
	for i in range(m):
		S[0][i] = abs(i - A[0] + 1)
	#S[0]에 A[0]의 연산횟수 저장
	
	for i in range(1, n):
		for j in range(m):
			S[i][j] = min(S[i - 1][:j + 1]) + abs(j + 1 - A[i])

	return min(S[len(A)-1])
	
A = [int(x) for x in input().split()]
print(solve(A))

'''
j+1는 1부터 최대값까지의 숫자이고,
S에는 A[i]가 j+1일 때의 최소 연산횟수를 저장한다.
먼저, S[0]에는 A[0]가 j+1일 때의 연산횟수를 저장한다.
A[i]가 j+1이 되는 최소 연산횟수는 
S[i-1][:j+1]까지의 값들 중 최소 연산 횟수와 A[i]를 j로 만드는 연산 횟수이다.
점화식은 S[i][j] = min(S[i][:j+1])+abs(j+1-A[i])이다.
'''
'''
수행시간은 M이 A배열의 최대값일 때
S[0]의 값을 구하기 위해 M번의 반복을 하고
dp테이블의 값을 채우기 위해 Mn의 반복을 하며
나머지 연산들을 포함해 수행시간을 나타내면
T(n) = M+Mn+C이다.
이는 O(Mn)이다.
또한, 최악의 경우 정수값이 최대 200이므로
O(200n)이다.
'''