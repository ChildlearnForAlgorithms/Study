import math

def matrix_mult():
    for i in range(n):
    	for j in range(n):
            C[i][j] = math.inf # math module에서 제공하는 매우 큰 정수
            for k in range(i, j):
                cost = min(C[i][k]+C[k+1][j]+P[i]*P[k+1]*P[j+1])
                if cost<C[i][j]:
                    C[i][j] = cost
    return C[1][n-1]

n = int(input()) # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
P = [int(x) for x in input().split()] # M_i = p_i x p_{i+1}
C = [[0]*n for _ in range(n)] # 비용을 저장할 2차원 리스트 C 초기화
min_cost = matrix_mult()
print(min_cost)