'''
<考察>
ある桁に対して、

&1 --- 何もしない
&0 --- 0にする
|1 --- 1にする
|0 --- 何もしない
^1 --- 何もしない
^0 --- 1->0, 0->1

なので、考えるのは

&0 - 0にする
|1 - 1にする
^0 - 反転
(^0^0 = 意味無し、&0^0 = |1、|1^0 = &0)

'''

N, C = map(int, input().split())
X = [(C>>i)%2 for i in range(30)]

# op : オペレーション配列
# 0 -> x = 0 (&0)
# 1 -> x = 1 (|1)
# 2 -> 反転 (^1)
# 3 -> do nothing

op = [3] * 30

# opのi番目の桁に操作を行う
def manipulate(val, t, b):
    if t == 1 and b == 0: # &0
        return 0
    if t == 2 and b == 1: # |1
        return 1
    if t == 3 and b == 1: # ^1
        if val == 0:
            return 1
        if val == 1:
            return 0
        if val == 2:
            return 3
        if val == 3:
            return 2
    # 何も引っかからなかった場合
    return val

def ap(val, op):
    if op == 0: return 0
    if op == 1: return 1
    if op == 2: return val ^ 1
    if op == 3: return val
    

for _ in range(N):
    T, A = map(int, input().split())
    tmp = 0
    for i in range(30):
        op[i] = manipulate(op[i], T, (A>>i)%2)
        X[i] = ap(X[i], op[i])
        tmp += X[i] << i
    print(tmp)