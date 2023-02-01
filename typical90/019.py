N = int(input())
N *= 2
A = list(map(int, input().split()))

dp = [[10**10] * (N + 1) for _ in range(N + 1)]
for i in range(N+1):
    dp[i][i] = 0

for w in range(2, N+1, 2):
    for l in range(N+1):
        r = l + w
        if r > N:
            break
        dp[l][r] = min(dp[l][r], dp[l+1][r-1]+abs(A[l]-A[r-1]))
        for i in range(l+2, r-1, 2):
            dp[l][r] = min(dp[l][r], dp[l][i]+dp[i][r])

print(dp[0][N])
