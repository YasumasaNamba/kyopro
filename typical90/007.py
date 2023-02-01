"""
番兵の値を工夫する
"""
N = int(input())
A = [-10**10] + list(map(int, input().split())) + [10**10]
A.sort()

Q = int(input())
for _ in range(Q):
    B = int(input())
    l, r = -1, len(A)
    while r - l > 1:
        m = (r + l) // 2
        if A[m] >= B:
            r = m
        else:
            l = m
    print(min(B - A[l], A[r] - B))