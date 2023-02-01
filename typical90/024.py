N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = sum([abs(A[i]-B[i]) for i in range(N)])
if (cnt <= K) and ((K-cnt) % 2 == 0):
    print('Yes')
else:
    print('No')