import itertools as it
import math

N, X = map(int, input().split())


A = [list(map(int, input().split()))[1:] for _ in range(N)]
cnt = 0
for i in it.product(*A):
    if X == math.prod(i):
        cnt += 1

print(cnt)
