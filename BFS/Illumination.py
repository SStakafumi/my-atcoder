from collections import deque

# directions[0] は偶数行の隣接マス
# directions[1] は奇数業の隣接マス
directions = [[(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (1, 1)],
              [(-1, -1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1)]]

# 入力
# board は外周に道マスを付け加えて、さらにその外側に壁マスを付け加える
W, H = map(int, input().split())
board = []
for y in range(H + 4):
    if y == 0 or y == H + 3:
        board.append([1]*(W + 4))
    elif y == 1 or y == H + 2:
        board.append([1] + [0]*(W + 2) + [1])
    else:
        board.append([1, 0] + list(map(int, input().split())) + [0, 1])

# BFS開始
# グラフの頂点と辺の数を数える
checked = [[False]*(W + 4) for _ in range(H + 4)]
q = deque([(1, 1)])
checked[1][1] = True
v, e = 0, 0  # v:頂点, e:辺
while q:
    x, y = q.popleft()
    v += 1  # 頂点(というか道ブロックのカウント値)を＋1
    for dx, dy in directions[y & 1]:
        nx, ny = x + dx, y + dy
        if board[ny][nx] == 1:  # 隣接するブロックが建物ないしは壁だと何もしない
            continue
        e += 1  # 隣接するブロックが道だと辺を＋1
        if not checked[ny][nx]:
            checked[ny][nx] = True
            q.append((nx, ny))
e /= 2


ans = 6 * v - 2 * int(e) - 4 * (W + 2) - 4 * (H + 2) + 2  # 道の全周囲から外枠の周囲を取る
print(ans)
