# 解法1 1.24s
""" 
from itertools import permutations


def threat(x1, y1, x2, y2):
    return (x1 == x2) or (y1 == y2) or (abs(x1-x2) == abs(y1-y2))


N = 8
answers = []

for combo in permutations(range(N)):
    board1 = [(i, c) for i, c in enumerate(combo)]
    board2 = [board1[i+1:] for i in range(N) if i < N-1]
    tmp = 0
    for i, (y1, x1) in enumerate(board1):
        if i == N-1:
            break
        flg = True
        for y2, x2 in board2[i]:
            if threat(x1, y1, x2, y2):
                flg = False
        if flg:
            tmp += 1
    if tmp == N-1:
        answers.append(combo)
        # for z in board1:
        #    print(' _ ' * z[1] + ' Q ' + ' _ ' * (8-z[1]-1))
        #    print('')
        # break

N = int(input())
X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


for oneAns in answers:
    for x, y in zip(X, Y):
        if oneAns[x] != y:
            break
    else:
        ans = oneAns
        break

for y in ans:
    l = ["."]*8
    l[y] = "Q"
    print("".join(l))
"""

# 解法2 (解法1を改造) こっちの方がループが少なく早い 0.35s
""" 
import itertools as it

def threat(x1, y1, x2, y2):
    return (x1 == x2) or (y1 == y2) or (abs(x1-x2) == abs(y1-y2))


answers = []
for perm in it.permutations(range(8)):
    qPos = [[x, y] for x, y in enumerate(perm)]
    for comb in it.combinations(qPos, 2):
        if threat(*comb[0], *comb[1]):
            break
    else:
        answers.append(perm)


N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for oneAns in answers:
    for x, y in zip(X, Y):
        if oneAns[x] != y:
            break
    else:
        ans = oneAns
        break

for y in ans:
    l = ["."]*8
    l[y] = "Q"
    print("".join(l))
"""

# 解法3 よくわからん
""" 
N = 8
count = 0
answers = []
for combo in it.permutations(range(N)):
    s1 = set(combo[i]+i for i in range(N))
    s2 = set(combo[i]-i for i in range(N))
    if N == len(s1) == len(s2):
        answers.append(combo)
print(count)
 """

# 解法4 よくわからん 圧倒的にはやい
count = 0  # 駒の置き方が何通りか格納する変数
board = []  # 盤上に置かれた駒を表すリスト


def deplication(x, y):
    """斜めの重複チェック"""
    for x1 in range(0, x):
        y1 = board[x1]
        if abs(x - x1) == abs(y - y1):
            return True
    return False


def n_queen(n, x):
    """
    xはクイーンを配置する行
    yはクイーンを配置する列
    1行ずつ配置していき最後の行まで配置できたらcountを+1する
    """
    global count
    if n == x:
        # print(board)
        count += 1
    else:
        for y in range(0, n):
            if y in board or deplication(x, y):
                continue
            board.append(y)
            n_queen(n, x + 1)
            board.pop()


n_queen(8, 0)
print(count)
