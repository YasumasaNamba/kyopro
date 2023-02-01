from heapq import heapify, heappush, heappop

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append((B, C))
    edges[B].append((A, C))

def dijkstra(start):
    pq = [(0, start)]
    heapify(pq)
    dist = [None] * (N + 1)

    for _ in range(N):
        while True:
            d, pos = heappop(pq)
            if dist[pos] is None:
                break
        dist[pos] = d
        for to_pos, to_d in edges[pos]:
            heappush(pq, (d+to_d, to_pos))
    return dist

dist1 = dijkstra(1)
distN = dijkstra(N)

for i in range(1, N+1):
    print(dist1[i] + distN[i])
    

