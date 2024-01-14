from itertools import combinations
from collections import defaultdict


def distance(x, y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2


def check_square(a, b, c, d):
    dis_cnt = defaultdict(int)
    for x, y in combinations((a, b, c, d), 2):
        dis = distance(x, y)
        dis_cnt[dis] += 1
    if max(dis_cnt.values()) == 4 and min(dis_cnt.values()) == 2:
        return True
    else:
        return False


pon_pos = []
for i in range(9):
    s_tmp = input()
    for j, s in enumerate(s_tmp):
        if s == '#':
            pon_pos.append((i, j))

ans = 0
for a, b, c, d in combinations(pon_pos, 4):
    ans += int(check_square(a, b, c, d))

print(ans)
