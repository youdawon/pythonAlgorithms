import heapq

INF = float("inf")

def dijkstra(n, edges, start):

  ## 인접 리스트 생성 
  graph = [ [] for _  in range(n+1)]
  for u, v, w in edges:
    graph[u].append((v, w))

  ## 모든 거리를 무한대로 설정한다 시작 도시는 0으로 설정한다. 
  distances = [ INF for _ in range(n+1) ]
  distances[start] = 0

  ## 가장 짧은 거리를 추출할 우선순위 큐를 생성한다. 
  priority_queue = [(start, 0)]

  while priority_queue:
    current_node, current_distance = heapq.heappop(priority_queue)

    ##현재 거리가 이전에 저장된 동일한 도시의 거리보다 큰지 확인한다. 
    ## 클 경우 데이터를 저장하지않고 다음으로 넘어간다. 
    if current_distance > distances[current_node]:
      continue

    ## 작을 경우 해당 노드의 인접행렬을 모두 검색해서 가장 작은 값으로 거리를 업데이트한다.
    for neighbor, weight in graph[current_node]:
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(priority_queue, (neighbor, distance))
        
  return distances

edges = []
#n, m : 도시수(vertex), 거리수(edges)
n, m = 5, 6
## u : 시작도시 v:도착도시, w:가중치
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