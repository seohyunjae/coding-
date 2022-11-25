def dfs(graph, v, visited):
    visited[v] = T
    print(v, end='')
    for i in graph[v]:
        if F == visited[i]:
            dfs(graph, i, visited)
    

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]

]

visited = [F] * 9
dfs(graph, 1, visited)