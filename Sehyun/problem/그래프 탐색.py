n,m=map(int,input().split())
graph=[
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]
visited=[False for _ in range(n+1)]

start_points=[]
end_points=[]

for _ in range(m):
    s,e=map(int,input().split())
    start_points.append(s)
    end_points.append(e)

for start,end in zip(start_points,end_points):
    graph[start][end]=1
    graph[end][start]=1

cnt=0
def dfs(vertex):
    global cnt
    for curr_v in range(1,n+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            cnt+=1
            visited[curr_v]=True
            dfs(curr_v)

root_vertex=1
visited[root_vertex]=True
dfs(root_vertex)

print(cnt)