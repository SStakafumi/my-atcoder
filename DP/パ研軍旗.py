import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
flag = [[] for _ in range(N)]
for i in range(5):
    row = list(input())
    for j in range(N):
        flag[j].append(row[j])

# dp[i][j] = i列目までを考えたときに、最後の列の色がjであるものの中で、塗り替えるますの個数の最小値
# R : 0, B : 1, W : 2
dp = [[0]*3 for _ in range(N)]

for i in range(N):  # 0,1,2,..,N-1列目
    # i列目で赤、青、白に塗るべき枚数
    rbw = [5-flag[i].count('R'), 5-flag[i].count('B'),
           5-flag[i].count('W')]
    # 1列目の時はただ塗って終了
    if i == 0:
        for j in range(3):
            dp[0][j] = rbw[j]
    else:
        dp[i][0] = rbw[0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = rbw[1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = rbw[2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))
