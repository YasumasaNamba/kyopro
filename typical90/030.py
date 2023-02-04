N, K = map(int, input().split())

d = [0] * (N + 10)
for i in range(2, N+1):
    if d[i] > 0:
        continue
    for j in range(i, N+1, i):
        d[j] += 1

ans = sum([1 for i in range(2, N+1) if d[i]>=K])
print(ans)