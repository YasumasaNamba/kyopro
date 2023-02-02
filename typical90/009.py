from functools import cmp_to_key
import math

def compare(p1, p2):
    is_upper1 = (p1[1] > 0) or (p1[1] == 0 and p1[0] >= 0)
    is_upper2 = (p2[1] > 0) or (p2[1] == 0 and p2[0] >= 0)

    if is_upper1 != is_upper2:
        if is_upper1: return -1
        else: return 1
    
    cross = p1[0] * p2[1] - p1[1] * p2[0]
    # if cross == 0:
    #     return abs(p1[0] + p1[1]) - abs(p2[0] + p2[1])
    return cross

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

def angle(p):
    norm = (p[0]**2 + p[1]**2) ** 0.5
    deg = math.acos(p[0]/norm) * 180 / math.pi
    if p[1] < 0:
        deg = 360 - deg
    return deg

ans = 0
for i in range(N):
    newP = []
    for j in range(N):
        if i == j:
            continue
        newP.append([P[j][0]-P[i][0], P[j][1]-P[i][1]])
    # newP.sort(key=cmp_to_key(compare))
    newP_angle = [angle(p) for p in newP]
    len_P = len(newP_angle)
    for j in range(len_P):
        l, r = -1, len_P
        while r - l > 1:
            m = (r + l) // 2
            if newP_angle[m] >= (180 - newP_angle[j]):
                r = m
            else:
                l = m
        a = max(abs(newP_angle[j]-newP_angle[(m-1)%len_P]), abs(newP_angle[(m+1)%len_P]-newP_angle[j]))
        ans = max(ans, min(a, 360-a))
print(ans)

