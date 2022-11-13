W = int(input())
words = input().split()
# code below
dp = [0 for _ in range(len(words))]  # words 리스트 길이만큼 dp 배열을 생성해줌
dp[0] = (W - len(words[0])) ** 3  # 첫 번째 단어의 penalty 값을 저장해줌

for i in range(1, len(words)):
    min_penalty = dp[i - 1] + (W - len(words[i])) ** 3
    word_length = len(words[i])
    for j in range(i, 0, -1):
        word_length += len(words[j - 1]) + 1  # 공백을 포함하기 위해 +1
        if word_length - 1 >= W:  # 단어의 길이가 페이지 폭을 넘어가면 안됨
            break
        curr_penalty = dp[j - 2] + (W - word_length) ** 3
        min_penalty = min(min_penalty, curr_penalty)  # 순차적으로 비교하며 최소 penalty 값을 찾아줌
    dp[i] = min_penalty  # dp에 최소 penalty 값을 저장해줌

print(dp[-1])  # dp의 마지막 값을 출력
'''
알고리즘 설명 및 수행시간 분석

최소 penalty 값을 만들어주기 위해서는 해당 줄의 글자 수가 길수록 penalty 점수가 작아진다. words 리스트의
i번째 값으로 순차적으로 penalty를 계산해서 순차적으로 현재의 penalty값과 최소 penalty값을 비교해준다.
dp[i]에는 i번째 단어까지의 최소 패널티를 저장해주어 결과값은 dp의 가장 마지막 값을 출력해준다.

이 코드에서 가장 수행시간에 영향을 미치는 것은 이중 for문이므로 이 코드의 수행시간을 점화식으로 표현하자면
T(n)=Cn^2+D(C와 D는 상수)이므로 수행시간을 Big-O로 표기하면 O(n^2)이다.
'''
