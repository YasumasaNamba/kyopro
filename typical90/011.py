N = int(input())
DCS = [list(map(int, input().split())) for _ in range(N)]
DCS.sort()

dp = [[0] * 5001 for _ in range(N+1)]
for i in range(1, N+1):
    D, C, S = DCS[i-1]
    for j in range(5000, 0, -1):
        if j - C >= 0 and j <= D:
          dp[i][j] = max(dp[i-1][j], dp[i-1][j-C] + S)
          print(i, j, D, C, S, dp[i][j])

print(max(dp[N]))

