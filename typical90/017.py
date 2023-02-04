N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]
lines.sort(key=lambda x: (x[1], -x[0]))

def bit_add(bit, pos):
    pos += 1
    while pos < len(bit):
        bit[pos] += 1
        pos += pos & -pos

def bit_get(bit, pos):
    pos += 1
    res = 0
    while pos > 0:
        res += bit[pos]
        pos -= pos & -pos
    return res

bitl = [0] * (N + 1)
bitr = [0] * (N + 1)

ans = 0
for l, r in lines:
    ans += bit_get(bitl, l-1) - bit_get(bitr, l)
    bit_add(bitl, l)
    bit_add(bitr, r)

print(ans)
