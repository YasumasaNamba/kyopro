from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [[0] * N for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    XY[X][Y] = 1
    XY[Y][X] = 1

ans = 10**18
for order in permutations(range(N)):
    ok = True
    score = 0
    for i in range(N-1):
        score += A[order[i]][i]
        if XY[order[i]][order[i+1]] == 1:
            ok = False
            break
    score += A[order[N-1]][N-1]
    if ok:
        ans = min(ans, score)

if ans == 10**18:
    print(-1)
else:
    print(ans)
    


