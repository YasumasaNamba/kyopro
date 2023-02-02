N = int(input())
DCS = [list(map(int, input().split())) for _ in range(N)]
DCS.sort()
INF = 10 ** 18

dp = [[-INF] * 5001 for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    D, C, S = DCS[i]
    for j in range(5001):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j + C <= D:
            dp[i+1][j+C] = max(dp[i+1][j+C], dp[i][j] + S)
        
print(max(dp[N]))