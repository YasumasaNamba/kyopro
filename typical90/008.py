N = int(input())
S = input()
atcoder = 'atcoder'
MOD = 10 ** 9 + 7

dp = [[0] * 8 for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(8):
        dp[i][j] = dp[i-1][j]
        if j - 1 >= 0 and atcoder[j-1] == S[i-1]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= MOD

print(dp[N][7])