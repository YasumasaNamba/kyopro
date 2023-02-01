N = int(input())

seg_len = 1 << 17
seg1 = [0] * (1 << 18)
seg2 = [0] * (1 << 18)

def set_value(seg, x, pos):
    pos += seg_len
    seg[pos] = x
    while pos > 0:
        pos //= 2
        seg[pos] = seg[pos*2] + seg[pos*2+1]

def get_value(seg, l, r):
    l += seg_len
    r += seg_len
    v = 0
    while r > l:
        if l % 2 == 1:
            v += seg[l]
            l += 1
        l //= 2
        if r % 2 == 1:
            v += seg[r-1]
            r -= 1
        r //= 2
    return v

def get_value2(seg, ql, qr, sl=0, sr=seg_len, pos=1):
    if ql <= sl and sr <= qr:
        return seg[pos]
    elif qr <= sl or sr <= ql:
        return 0
    else:
        m = (sl + sr) // 2
        v1 = get_value2(seg, ql, qr, sl, m, pos*2)
        v2 = get_value2(seg, ql, qr, m, sr, pos*2+1)
        return v1 + v2

for i in range(1, N+1):
    C, P = map(int, input().split())
    if C == 1:
        set_value(seg1, P, i)
    else:
        set_value(seg2, P, i)

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(get_value(seg1, L, R+1), get_value(seg2, L, R+1))