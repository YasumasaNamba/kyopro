N = int(input())
A, B, C = map(int, input().split())
A, B, C = sorted([A, B, C], reverse=True)

ans = 10000
for i in range(10000):
    for j in range(10000-i):
        if N - A * i - B * j < 0:
            break
        k, m = divmod(N - A * i - B * j, C)
        if m == 0:
            ans = min(ans, i + j + k)
print(ans)

