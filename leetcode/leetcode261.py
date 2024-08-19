"""
261. Graph Valid Tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
def isGraphValidTree(n, edges):

  ## 인접리스트 생성
  graph = [ [] for _ in range(n) ]
  for first, second in edges:
    graph[first].append(second)
    graph[second].append(first)

  visited = [ -1 for _ in range(n) ]

  if not dfs(graph, visited, 0, -1):
    return False

  return all(visited)

def dfs(graph, visited, current, parent):

  if visited[current] == 1:
    return True

  if visited[current] == 0:
    return False 

  visited[current] = 0

  for neighbor in graph[current]:
    if parent == neighbor:
      continue
    if not dfs(graph, visited, neighbor, current):
      return False

  visited[current] = 1

  return True
n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# n = 4
# edges = [[0, 1], [0, 2], [2, 3]]


print(isGraphValidTree(n, edges))