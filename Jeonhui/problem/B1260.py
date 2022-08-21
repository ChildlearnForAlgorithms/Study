'''
DFS BFS
그래프 전체를 탐색하는 방법 중 하나. (완벽히 탐색)
시작점 부터 다음 branch로 넘어가기 전에 해당 branch를 완벽하게 탐색하고 넘어가는 방법
재귀함수나 스택으로 구현
탐색 시작 노드를 스택에 삽입하고 방문처리
스택에 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리
방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
2번 과정을 수행할 수 없을 때까지 반복
방문 여부를 반드시 검사

'''


def dfs(s):
    visitDFS[s - 1] = True
    print(s, end=" ")
    for p, c in A:
        if c == s and not visitDFS[p - 1]:
            dfs(p)
        if p == s and not visitDFS[c - 1]:
            dfs(c)


def bfs(s):
    q = [s]
    visitBFS[s - 1] = True
    while len(q)!=0:
        c = q[0]
        q.pop()
        print(c)
        for p,c in A:
            next = A[]

n, m, v = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
visitDFS = [False] * n
visitBFS = [False] * n
dfs(v)
