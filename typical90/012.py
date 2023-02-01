H, W = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.p = [-1] * (n + 1)
        self.r = [1] * (n + 1)
    
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
    
    def find(self, x):
        if self.p[x] == -1:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

def turn_red(q):
    r, c = q[1], q[2]
    r -= 1
    c -= 1
    is_red[r * W + c] = 1
    for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        nxt_r = r + y
        nxt_c = c + x
        if 0 <= nxt_r <= H - 1 and 0 <= nxt_c <= W - 1:
            if is_red[nxt_r * W + nxt_c] == 1:
                uf.unite(r * W + c, nxt_r * W + nxt_c)


uf = UnionFind(H * W)
is_red = [0] * (H * W + 1)
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        turn_red(q)
    elif q[0] == 2:
        r1, c1, r2, c2 = q[1:]
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        if (uf.find(r1 * W + c1) == uf.find(r2 * W + c2)) and (is_red[r1 * W + c1] == is_red[r2 * W + c2] == 1):
            print('Yes') 
        else:
            print('No')