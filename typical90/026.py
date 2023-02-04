import sys
sys.setrecursionlimit(10**6)

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edges[A].append(B)
    edges[B].append(A)

dist = [None] * N

def dfs(now, n=0):
    if dist[now] is not None:
        return
    dist[now] = n
    for to in edges[now]:
        dfs(to, (n+1)%2)
dfs(0)
idx_0 = [i+1 for i in range(N) if dist[i]==0]
idx_1 = [i+1 for i in range(N) if dist[i]==1]

if len(idx_0) >= N//2:
    print(*idx_0[:N//2])
else:
    print(*idx_1[:N//2])