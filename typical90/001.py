N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

def isOK(m):
    l, r = 0, 1
    for _ in range(K+1):
        while A[r] - A[l] >= m:
            r += 1
            if r == len(A):
                return False
        l, r = r, r+1
    return True

# def isOK(m):
#     cnt = 0
#     l, r = 0, 1
#     while r <= N+1:
#         if A[r]-A[l] >= m:
#             l, r = r, r+1
#             cnt += 1
#         else:
#             r += 1
#     if cnt >= K+1:
#         return True
#     else:
#         return False
              
left, right = 0, L
while right - left > 1:
    m = (right + left) // 2
    if isOK(m):
        left = m
    else:
        right = m
print(left)