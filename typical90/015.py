N = int(input())
MOD = 10 ** 9 + 7

def mod_pow(a, b, p):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * mod_pow(a, b-1, p) % p
    elif b % 2 == 0:
        d = mod_pow(a, b//2, p)
        return d * d % p

fact = [1] * (N + 1)
inv_fact = [1] * (N + 1)

for i in range(1, N+1):
    fact[i] = i * fact[i-1] % MOD

inv_fact[N] = mod_pow(fact[N], MOD-2, MOD)
for i in range(N, 0, -1):
    inv_fact[i-1] = inv_fact[i] * i % MOD

def nCk(n, k):
    if k < 0 or n-k < 0:
        return 0
    return fact[n] * inv_fact[n-k] % MOD * inv_fact[k] % MOD

for k in range(1, N+1):
    ans = 0
    for i in range(1, N+1):
        n = N - (k-1) * (i-1)
        if n < i:
            break
        ans += nCk(n, i)
        ans %= MOD
    print(ans)
