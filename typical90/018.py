import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

def calc_pos(e):
    theta = 2 * math.pi * e / T
    y = -L / 2 * math.sin(theta)
    z = -L / 2 * math.cos(theta) + L / 2
    return y, z

def calc_degree(y, z):
    e1 = (X ** 2 + (Y - y) ** 2 + z **2) ** 0.5
    e2 = (X ** 2 + (Y - y) ** 2) ** 0.5
    return math.degrees(math.acos(e2/e1))

for _ in range(Q):
    E = int(input())
    y, z = calc_pos(E)
    print(calc_degree(y, z))