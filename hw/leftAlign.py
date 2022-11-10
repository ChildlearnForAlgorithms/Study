def align_left(W, words):
	dp = [0] * len(words)
	dp[0] = (W - len(words[0])) ** 3
	for i in range(1, len(words)):
		width = len(words[i])
		min_penalty = dp[i - 1] + (W - width) ** 3  # 다음 줄
		j = i
		while j > 0:
			width += (len(words[j-1]) + 1)
			penalty = dp[j - 2] + (W - width) ** 3 # j-1은 width에 더해짐
			if width > W:
				break
			if min_penalty > penalty:
				min_penalty = penalty
			j -= 1
		dp[i] = min_penalty
	print(dp[len(words) - 1])


W = int(input())
words = input().split()
align_left(W, words)

'''
DP 점화식은
width가 W를 넘지 않고, 가장 큰 넓이를 가지는 수를 찾아야 한다.
DP[i] = dp[j-2]+(W-width)**3 와 dp[i - 1] + (W - width) ** 3 중 가장 작은 값이다.
수행시간은
for문 안에 while문이 최악의 경우 i번씩 돌아가기 때문에 
1+2+3+...+n-1이 되고 
O(n^2)이다.
'''
