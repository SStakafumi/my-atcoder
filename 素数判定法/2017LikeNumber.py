def Eratosthenes(n):
    """n以下の素数をエラトステネスの篩によって求める.リストをかえす"""
    prime = []
    limit = n**0.5
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


# エラトステネスで素数リストを作成
_primes = Eratosthenes(10**5)
primes = [False] * (10**5+1)

for p in _primes:
    primes[p] = True

like_2017 = [False] * (10**5+1)

for p in _primes:
    if primes[(p+1)//2]:
        like_2017[p] = True

c = 0
C = [0]
for i in range(1, 10**5+1):
    if like_2017[i]:
        c += 1
    C.append(c)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(C[r]-C[l-1])
