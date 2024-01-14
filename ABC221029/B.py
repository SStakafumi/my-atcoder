a, b, c, d, e, f = list(map(int, input().split()))

dm = 998244353

ans = (((a % dm) * (b % dm) * (c % dm)) %
       dm - ((d % dm) * (e % dm) * (f % dm)) % dm) % dm

if ans < 0:
    print(ans%dm)
else:
    print(ans)