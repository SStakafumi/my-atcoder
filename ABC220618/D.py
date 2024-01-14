import itertools
import math
from collections import Counter
import heapq
from collections import deque
from pprint import pprint
import sys
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

sys.setrecursionlimit(6 * 10 ** 5)
def input(): return sys.stdin.readline().rstrip()


N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
print(LR)

ims = [0] * (2 * 10 ** 5 + 1)

for l, r in LR:
    ims[l] += 1
    ims[r] -= 1

S = []

last = -1

current = 0

for i in range(1, 2 * 10 ** 5 + 1):
    if current == 0 and current + ims[i] > 0:
        last = i
    elif current + ims[i] == 0 and current > 0:
        S.append([last, i])
    current += ims[i]

    # print(ims,current)
# print(ims,current)

for x, y in S:
    print(x, y)
