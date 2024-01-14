from itertools import product

R, C = map(int, input().split())
lines = list(zip(*[list(map(int, input().split())) for _ in range(R)]))

# ans = 0

# for p in product((0, 1), repeat=R):
#     buckNum = 0
#     for line in lines:
#         cnt = 0
#         for r in range(R):
#             if p[r] == line[r]:
#                 cnt += 1
#         buckNum += max(cnt, R-cnt)
#     ans = max(ans, buckNum)

# print(ans)
