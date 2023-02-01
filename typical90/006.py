from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
S = input()

pq = []
heapify(pq)

for i in range(N-K):
    heappush(pq, ord(S[i]) * 1000000 + i)

ans = ''
last_idx = -1
for i in range(N-K, N):
    heappush(pq, ord(S[i]) * 1000000 + i)
    while True:
        n = heappop(pq)
        if n % 1000000 > last_idx:
            break
    ans += chr(n // 1000000)
    last_idx = n % 1000000

print(ans)