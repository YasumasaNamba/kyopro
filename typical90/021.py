N, M = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.p = [-1] * (n + 1)
        self.r = [1] * (n + 1)
        self.l = [1] * (n + 1)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.r[x] > self.r[y]:
            x, y = y, x
        if self.r[x] == self.r[y]:
            self.r[y] += 1
        self.p[x] = y
        self.l[y] += self.l[x]
    
    def find(self, x):
        if self.p[x] == -1:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def len(self, x):
        x = self.find(x)
        return self.l[x]
    
uf = UnionFind(N)
AB = []
for _ in range(M):
    A, B = map(int, input().split())
    if A > B:
        AB.append((A, B))
    else:
        AB.append((B, A))
AB.sort()

for i in range(len(AB)-1):
    if AB[i] == AB[i+1]:
        uf.unite(AB[i][0], AB[i][1])

ans = 0
used = [0] * (N + 1)
for i in range(1, N+1):
   i = uf.find(i)
   if used[i] == 1:
       continue
   used[i] = 1
   n = uf.len(i)
   print(n)
   ans += n * (n - 1) // 2
print(ans)
print(uf.p)


