from functools import lru_cache


@lru_cache(maxsize=1_000_000)
N = int(input())


def f(k):
    if k == 0:
        return 1
    else:
        return f(k//2) + f(k//3)


print(f(N))
