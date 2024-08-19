"""
323. Number of Connected Components in an Undirected Graph
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

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