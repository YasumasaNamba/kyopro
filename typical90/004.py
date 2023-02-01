H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row_sum = [0] * H
col_sum = [0] * W
for i in range(H):
    row_sum[i] = sum([A[i][j] for j in range(W)])
for j in range(W):
    col_sum[j] = sum([A[i][j] for i in range(H)])

for i in range(H):
    for j in range(W):
        print(row_sum[i] + col_sum[j] - A[i][j], end=' ')
    print()