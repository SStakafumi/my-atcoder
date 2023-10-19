from itertools import permutations, combinations

while True:
    ans = 0
    n, x = map(int, list(input().split()))
    if n==0 and x==0:
        flag=False
        break
    for tmp in combinations(list(range(1, n+1)), 3):
        if sum(tmp) == x:
            ans += 1
    print(ans)
    