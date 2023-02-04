N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
redge = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    edge[A].append(B)
    redge[B].append(A)

come = [0] * (N + 1)
backorder = []

def dfs(x):
    come[x] = 1
    for to in edge[x]:
        if come[to]:
            continue
        dfs(to)
    backorder.append(x)

components = []

def rdfs(x):
    come[x] = 1
    components[-1].append(x)
    for to in redge[x]:
        if come[to]:
            continue
        rdfs(to)

for v in range(1, N+1):
    if come[v]:
        continue
    dfs(v)

backorder.reverse()
come = [0] * (N + 1)
for v in backorder:
    if come[v]:
        continue
    components.append([])
    rdfs(v)

ans = 0
for c in components:
    n = len(c)
    ans += n * (n - 1) // 2
print(ans)