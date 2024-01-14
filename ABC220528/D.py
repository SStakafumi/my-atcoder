def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


N, A, B = map(int, input().split())

ans = N * (N + 1) // 2

L = lcm(A, B)
NA = N // A
NB = N // B
NL = N // L
ans -= NA * (NA + 1) // 2 * A
ans -= NB * (NB + 1) // 2 * B
ans += NL * (NL + 1) // 2 * L


print(ans)
