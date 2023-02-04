N = int(input())
name_dict = {}
ans = []

for i in range(1, N+1):
    S = input()
    if name_dict.get(S, 0) == 0:
        name_dict[S] = 1
        ans.append(i)

for a in ans:
    print(a)

