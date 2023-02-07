from collections import defaultdict

N, K = map(int, input().split())
a = list(map(int, input().split()))

k = 0
used = defaultdict(int)
r = -1
ans = 0
for l in range(N):
    al = a[l]
    while r + 1 < N:
        r += 1
        ar = a[r]
        if used[ar] == 0 and k + 1 > K:
            r -= 1
            break
        elif used[ar] == 0 and k + 1 <= K:
            k += 1
            used[ar] += 1
        elif used[ar] > 0:
            used[ar] += 1
    ans = max(ans, r - l + 1)
    if used[al] == 1:
        k -= 1
    used[al] -= 1

print(ans)
