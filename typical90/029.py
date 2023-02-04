W, N = map(int, input().split())

seg_len = 1 << 19
seg = [0] * (1 << 20)

def set_value(ql, qr, sl=0, sr=seg_len, pos=1, h=None):
    if h is None:
        h = get_value(ql, qr) + 1
    if ql <= sl and sr <= qr:
        seg[pos] = h
        if sr - sl > 1:
            m = (sl + sr) // 2
            set_value(ql, qr, sl, m, pos*2, h)
            set_value(ql, qr, m, sr, pos*2+1, h)
    elif sr <= ql or qr <= sl:
        pass
    else:
        m = (sl + sr) // 2
        set_value(ql, qr, sl, m, pos*2, h)
        set_value(ql, qr, m, sr, pos*2+1, h)

def get_value(ql, qr):
    ql += seg_len
    qr += seg_len
    ans = 0
    while qr - ql > 0:
        if qr % 2 == 1:
            ans = max(ans, seg[qr-1])
            qr -= 1
        qr //= 2
        if ql % 2 == 1:
            ans = max(ans, seg[ql])
            ql += 1
        ql //= 2
    return ans

for _ in range(N):
    L, R = map(int, input().split())
    set_value(L, R+1)
    print(get_value(L, R+1))
