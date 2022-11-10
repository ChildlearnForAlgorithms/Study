def solve(L, S):
    D = [[1] * min(S, 9)] + [[0] * S for _ in range(L - 1)]
    for i in range(1, L):
        for j in range(S):
            D[i][j] = sum(D[i - 1][max(j - 9, 0):j + 1])
    return D[L - 1][S - 1]

L, S = [int(x) for x in input().split()] # 각 자리 수를
print(solve(L, S)%2147483647)

'''
DP테이블에는 각 자리 숫자 합이 S가 되는 값들의 개수를 저장한다.
D[0]는 한 자리 숫자의 합이 인덱스+1의 값이 되는 수의 개수이므로 D[0]에 모두 1을 저장해준다.
D[1]부터 D[L - 1]까지는 자릿수를 i라 할 때, i번째 수에는 0-9까지 올 수 있고,
i - 1번째 자릿수의 합이 j - 9부터 j의 값을 합친 수와 같다.
결론적으로 점화식은 D[i][j] = sum(D[i - 1][max(j-9, 0): j + 1])이 된다.
수행시간은 D[L - 1][S - 1]을 반환하므로 DP테이블을 채우는 수행시간과 같고
Tn= cLS +c이다. 이는 O(LS)의 수행시간을 가진다.
'''
