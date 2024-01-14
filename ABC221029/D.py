import os
import sys
from functools import lru_cache


@lru_cache(maxsize=1_000_000)
# 関数f
def f(x):
    if x == 0:
        return 1
    else:
        return f(x//2) + f(x//3)


N = int(input())

print(f(N))

# 別解
from collections import defaultdict
N = int(input())

memo_dict = defaultdict(int)
memo_dict[0] = 1

# 関数f


def f(x):
    if x == 0:
        return 1
    else:
        if memo_dict[x//2] != 0:
            f_2 = memo_dict[x//2]
        else:
            f_2 = f(x//2)
        if memo_dict[x//3] != 0:
            f_3 = memo_dict[x//3]
        else:
            f_3 = f(x//3)
        ans = f_2 + f_3
        memo_dict[x] = ans
        return ans


print(f(N))
