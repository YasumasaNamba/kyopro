import sys
sys.setrecursionlimit(10**6)

A, B, C = map(int, input().split())

def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x%y)

g = gcd(A, B)
g = gcd(g, C)
ans = A//g + B//g + C//g - 3
print(ans)

