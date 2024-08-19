def isGraphValidTree(n, edges) -> bool:

  graph = [[] for _ in range(n)]
  visited = [0 for _ in range(n)]

  ## 인접리스트 생성
  for first, second in edges:
    graph[first].append(second)
    graph[second].append(first)

  if not dfs(graph, visited, 0, -1):
    return False

  return all(visited)


def dfs(graph, visited, node, parent) -> bool:

  if visited[node] == -1:
    return False

  if visited[node] == 1:
    return True

  visited[node] = -1

  for neighbor in graph[node]:
    if neighbor == parent:
      continue    
    if not dfs(graph, visited, neighbor, node):
      return False

  visited[node] = 1

  return True


# n = 5
# edges = [[0, 1], [0, 2], [2, 3]]
n = 4
edges = [[0, 1], [0, 2], [2, 3]]


print(isGraphValidTree(n, edges))