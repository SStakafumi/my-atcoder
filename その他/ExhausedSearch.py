# TLE
""" 
N = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

for m in M:
    canSum = False
    for i in range(1 << N):
        l = []
        for k in range(N):
            if i >> k & 1:
                l.append(A[k])
            if m == sum(l):
                canSum = True
                break

    if canSum:
        print('yes')
    else:
        print('no')
 """

# 回答例1
""" 
import itertools as it

n, A = int(input()), list(map(int, input().split()))
yes_nums = set()
for bools in it.product([True, False], repeat=n):
    yes_nums.add(sum(A[i] for i in range(n) if bools[i]))

_ = input()
for m in map(int, input().split()):
    print("yes" if m in yes_nums else "no")
 """

# 回答例2 こっちのほうが早い

_ = input()
###### すべての和パターンを出すアルゴリズム ########
yes_nums = {0}
for x in map(int, input().split()):
    for y in [*yes_nums]:  # こうすることでfor中に'yes_num'の大きさが変わっても問題なくなる
        yes_nums.add(x + y)
        print(yes_nums)
####################################################

_ = input()
for m in map(int, input().split()):
    print("yes" if m in yes_nums else "no")
