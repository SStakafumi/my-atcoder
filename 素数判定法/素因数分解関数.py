def prime_factorize(n):
    '''素因数分解して素因数のリストを返す (1の時は空のリスト[]を返す)'''
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
print(*prime_factorize(n))
# print("{}:".format(n), *prime_factorize(n))
