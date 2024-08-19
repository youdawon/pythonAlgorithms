def countConnectedComponents(n, edges):

  count = 0

  ## 인접 리스트 생성
  graph = [ [] for _ in range(n) ]
  for first, second in edges:
    graph[first].append(second)
    graph[second].append(first)
  
  visited = [ -1 for _ in range(n) ]

  for i in range(len(graph)):
    if visited[i] == -1:
      count += 1
      dfs(graph, visited, i)

  return count

def dfs(graph, visited, i):

  if visited[i] == 1:
    return

  visited[i] = 1

  for neighbor in graph[i]:
    dfs(graph, visited, neighbor)

n = 5
# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
edges = [[0, 1], [1, 2], [3, 4]]

print(countConnectedComponents(n, edges))