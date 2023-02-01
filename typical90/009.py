import math

N = int(input())

points = []
XY = []

contain_origin = False
for i in range(N):
    X, Y = map(int, input().split())
    XY.append((X, Y))
    if X == 0 and Y == 0:
        contain_origin = True
    elif X == 0:
        points.append((0, 1, i))
    elif Y == 0:
        if X > 0:
            points.append((1, 0, i))
        else:
            points.append((-1, 0, i))
    else:
        d = (X**2 + Y**2)**0.5
        if X > 0 and Y > 0:
            points.append((X/d, Y/d, i))
        if X > 0 and Y < 0:
            points.append((-X/d, -Y/d, i)) 
        if X < 0 and Y > 0:
            points.append((X/d, Y/d, i)) 
        if X < 0 and Y < 0:
            points.append((-X/d, -Y/d, i)) 
points.sort()
for i in range(2):
    p = points[i]
    points.append()
if contain_origin:
    n = 2
else:
    n = 3

min_diff = 10**10
min_i = None
for i in range(N):
    ps = points[i:i+n]
    print(ps)
    diff = math.degrees(math.asin(ps[0][1])) - math.degrees(math.asin(ps[-1][1]))
    if diff < min_diff:
        min_diff = diff
        min_i = i
print(min_i)
print(points[min_i-n:min_i])