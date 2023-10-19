from collections import defaultdict
from bisect import bisect

n = int(input())
s_list = list(map(int, list(input())))

idx_list = defaultdict(list)

ans = 0

for i, s in enumerate(s_list):
    idx_list[s].append(i)

for fir_num in idx_list.keys():
    fir_num_idx = idx_list[fir_num][0]
    for sec_num in idx_list.keys():
        if bisect(idx_list[sec_num], fir_num_idx) < len(idx_list[sec_num]):
            sec_num_idx = idx_list[sec_num][bisect(idx_list[sec_num], fir_num_idx)]
            for third_num in idx_list.keys():
                if idx_list[third_num][-1] > sec_num_idx:
                    ans += 1

print(ans)


# 別解

n = int(input())
s = input()
point = 0

# 暗証番号を全探索する
for i in range(1000):
    # 右詰めで0埋め
    t = str(i).zfill(3)
    now = 0
    # sで暗証番号が作れるかを検証
    for j in s:
        if j == t[now]:
            now += 1
        if now == 3:
            point += 1
            break

print(point)