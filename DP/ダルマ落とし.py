# なんとなく理解してる
import sys
def input(): return sys.stdin.readline().rstrip()


def solve():
    while True:
        N = int(input())
        if N == 0:
            break
        W = list(map(int, input().split()))
        # 両閉区間[i,j]のブロックで取り除く事のできるブロック数の最大値
        dp = [[0]*N for _ in range(N)]
        for w in range(1, N):  # 幅は1,2,...,N-1
            for i in range(N-w):  # 開始端は0,1,2,...,N-w-1
                j = i+w
                # 区間の要素が偶数個だったら
                if w % 2 == 1:
                    # 間の[i+1,j-1]をすべてとりのぞけたら挟んでいるi番目とj番目が消せるかもしれない
                    if dp[i+1][j-1] == w-1:
                        # もし両端の差が1以下なら両端も消せる
                        if abs(W[i] - W[j]) <= 1:
                            dp[i][j] = w+1
                        # 両端の要素がちがったら両端をけさない
                        else:
                            dp[i][j] = w-1
                    for k in range(i+1, j):
                        newdp = dp[i][k]+dp[k+1][j]
                        if newdp > dp[i][j]:
                            dp[i][j] = newdp
                # 区間の要素が奇数個だったら
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        print(dp[0][-1])


solve()
