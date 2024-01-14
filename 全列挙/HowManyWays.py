from itertools import combinations

while True:
    n, x = map(int, input().split())
    if n+x == 0:
        break

    ans = 0
    l = [i for i in range(1, n+1)]
    for com in combinations(l, 3):
        if sum(com) == x:
            ans += 1

    print(ans)
