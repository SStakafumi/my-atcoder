# 解法1 幅優先(BFSで解く)

from collections import deque

h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]


dp = [[0]*w for _ in range(h)]
dp[0][0] = 1

d = deque([[0, 0]])

while d:  # dに一つでも要素が入っているときは処理を続ける
    if dp[h-1][w-1] != 0:
        break
    v = d.popleft()
    for sp in [[v[0], v[1]+1], [v[0]+1, v[1]]]:
        if sp[0] < h and sp[1] < w:
            if dp[sp[0]][sp[1]] != 0 or graph[sp[0]][sp[1]] == "#":
                continue
            if sp[0] == 0 or sp[1] == 0:
                dp[sp[0]][sp[1]] = 1
                d.append(sp)
            else:
                dp[sp[0]][sp[1]] = dp[sp[0]-1][sp[1]] + dp[sp[0]][sp[1]-1]
                d.append(sp)


# print(dp[h-1][w-1])
print(dp[h-1][w-1] % (10**9+7))


# # 解法2 BFSを使わない(こっちのほうが早い)
# H, W = map(int, input().split())

# graph = []
# for i in range(H):
#     graph.append(list(input()))

# # dp[i][j] = i行j番目に行く経路の数
# dp = [[0]*W for _ in range(H)]  # 0 を入れておくとらく
# dp[0][0] = 1

# for i in range(H):
#     for j in range(W):
#         if i == 0 and j == 0:
#             dp[i][j] = 1
#         elif i == 0:
#             if graph[i][j] == "#":
#                 # dp[i][j] = 0 (dpには初期値で0が入っているのでこう書かなくてもcontinueでよい)
#                 continue
#             else:
#                 dp[i][j] = dp[i][j-1]
#         elif j == 0:
#             if graph[i][j] == "#":
#                 # dp[i][j] = 0 (dpには初期値で0が入っているのでこう書かなくてもcontinueでよい)
#                 continue
#             else:
#                 dp[i][j] = dp[i-1][j]
#         elif graph[i][j] == "#":
#             # dp[i][j] = 0 (dpには初期値で0が入っているのでこう書かなくてもcontinueでよい)
#             continue
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]
#
# print(dp[H-1][W-1] % (10**9 + 7))
