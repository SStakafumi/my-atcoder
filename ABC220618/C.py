import sys
all = list(map(int, input().split()))
ans = 0

for t11 in range(1, 29):
    for t12 in range(1, 29):
        for t21 in range(1, 29):
            for t22 in range(1, 29):
                t13 = all[0]-t11-t12
                t23 = all[1]-t21-t22
                t31 = all[3]-t11-t21
                t32 = all[4]-t12-t22
                if (t13 > 0) and (t23 > 0) and (t31 > 0) and (t32 > 0):
                    if (all[5] - t13 - t23 > 0) and (all[2] - t31 - t32 > 0) and ((all[5] - t13 - t23) == (all[2] - t31 - t32)):
                        ans += 1
                else:
                    continue

print(ans)
