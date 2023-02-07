N, Q = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(N)]
xy_1 = sorted(xy, key=lambda x: x[0] + x[1])
xy_2 = sorted(xy, key=lambda x: x[0] - x[1])

def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

for _ in range(Q):
    q = int(input())
    pq = xy[q-1]
    d = max(dist(pq, xy_1[0]), dist(pq, xy_1[-1]), dist(pq, xy_2[0]), dist(pq, xy_2[-1]))
    print(d)