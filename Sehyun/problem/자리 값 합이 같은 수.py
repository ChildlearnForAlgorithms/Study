def solve(L, S):
    dp = [[0] * (1001) for _ in range(1001)]  # 값을 저장 할 dp테이블 생성
    for j in range(1, 10):  # 자리수가 1일 때 값 초기화
        dp[1][j] = 1
    for i in range(1, 1001):  # 합이 1일 때 값 초기화
        dp[i][1] = 1
    for i in range(2, 1001):
        for j in range(2, 10):  # j가 10보다 작을 때
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    for i in range(2, 1001):
        for j in range(10, 1001):  # j가 10이상일 때
            sum = 0
            for k in range(j - 9, j + 1):
                sum += dp[i - 1][k]  # 자리수가 i-1일 때 값을 이용하여 구하기
            dp[i][j] = sum
    return dp[L][S]


L, S = [int(x) for x in input().split()]

print(solve(L, S) % 2147483647)

'''
알고리즘 설명 : 

우선 2차원 DP 테이블을 생성해주었다. 자리수가 1일 때와, 합이 1일 때를 각각 초기화해주었다.
자릿수가 i일 때 자릿수의 합이 j가 되는 개수는 자리수가 i-1일 때의 경우를 참고하여 표현해줄 수 
있다. 자리수가 i-1일 때의 경우 앞에 i번째 자리 값에 1부터 9까지의 경우가 들어가도록 하면 되기
때문이다. 그리고 j가 9이하일 때와 9보다 클 때의 경우를 나누어서 문제를 해결해주었다.

이 코드의 수행시간을 결정하는 solve 함수에서 가장 수행시간에 영향을 미치는 것은 삼중 for문이므로
이 코드의 점화식은 T(n)=Cn^3+D(C와 D는 상수)이므로 수행시간을 Big-O로 표기하면 O(n^3)이다.

'''
