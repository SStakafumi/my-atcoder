import os
import sys
from itertools import combinations
from collections import defaultdict

# 点x と 点y の距離を求める
def distance_square(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2


# 点w, x, y, z が正方形か調べる
def check_square(w, x, y, z):
    dist_cnt = defaultdict(int)
    for target_x, target_y in combinations([w, x, y, z], 2):
        dist_square_xy = distance_square(target_x, target_y)
        dist_cnt[dist_square_xy] += 1

    if max(dist_cnt.values()) == 4 and min(dist_cnt.values()) == 2:
        return True
    else:
        return False


pone_idx = []
S = []
for i in range(9):
    s_i = input()
    for j, each_char in enumerate(s_i):
        if each_char == "#":
            pone_idx.append((i, j))

cnt = 0
for w, x, y, z in combinations(pone_idx, 4):
    cnt += int(check_square(w, x, y, z))

print(cnt)
