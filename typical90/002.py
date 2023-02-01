N = int(input())

if N % 2 == 1:
    exit()

ans = [('', 0, 0)]
for _ in range(N):
    tmp = []
    for s, l, r in ans:
        if l == N//2:
            tmp.append((s+')', l, r+1))
        elif l < N//2 and l == r:
            tmp.append((s+'(', l+1, r))
        elif l < N//2 and l > r:
            tmp.append((s+'(', l+1, r))
            tmp.append((s+')', l, r+1))
    ans = tmp.copy()
for a in ans:
    print(a[0])
        
        