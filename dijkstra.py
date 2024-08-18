import heapq

INF = float('inf')

def dijkstra(n, edges, start):

  graph = [ [] for _ in range(n+1)]

  for u, v, w in edges:
    graph[u].append((v, w))

  distances = [ INF for _ in range(n+1) ]
  distances[start] = 0
  
  priority_queue = [(start, 0)]

  while priority_queue:
    current_node, current_distance = heapq.heappop(priority_queue)

    if current_distance > distances[current_node]:
      continue
    
    for neighbor, weight in graph[current_node]:
      distance = current_distance + weight
    
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(priority_queue, (neighbor, distance))

  return distances


edges = []
#n, m : 도시수(vertex), 거리수(edges)
n, m = 5, 6
## u, v, w : u : 시작도시 v:도착도시, w:가중치
edges.append((1,2,2))
edges.append((1,3,5))
edges.append((2,3,1))
edges.append((2,4,2))
edges.append((3,5,3))
edges.append((4,5,1))

start = 1

# 다익스트라 알고리즘 실행
distances = dijkstra(n, edges, start)

# 결과 출력
for i in range(1, n + 1):
  if distances[i] == INF:
      print("INF")
  else:
      print(distances[i])