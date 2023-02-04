N = int(input())

m = [[0] * 1002 for _ in range(1002)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    m[lx][ly] += 1
    m[lx][ry] -= 1
    m[rx][ly] -= 1
    m[rx][ry] += 1

for i in range(1001):
    for j in range(1001):
        m[i][j+1] += m[i][j]

for j in range(1001):
    for i in range(1001):
        m[i+1][j] += m[i][j]

ans = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        ans[m[i][j]] += 1

for i in range(1, N+1):
    print(ans[i])