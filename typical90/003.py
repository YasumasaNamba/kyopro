import sys
sys.setrecursionlimit(10**6)

N = int(input())
edge = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

dist = [0] * (N + 1)

def dfs(now, last=-1):
    global dist
    for to in edge[now]:
        if to == last:
            continue
        dist[to] = dist[now] + 1
        dfs(to, now)

dfs(1)
max_dist = max(dist)
farest = dist.index(max_dist)

dist[farest] = 0
dfs(farest)
print(max(dist)+1)