from collections import defaultdict
import itertools
import math
from collections import Counter
import heapq
from collections import deque
from pprint import pprint
import sys
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

sys.setrecursionlimit(6 * 10 ** 5)
def input(): return sys.stdin.readline().rstrip()


N = int(input())
S = list(input())
W = list(map(int, input().split()))
WS = set(W)
W_sorted_unique = sorted(list(WS))
adult_num = len([s for s in S if s == "1"])
child_num = len(S) - adult_num
w_child_adult_dict = defaultdict(list)
for s, w in zip(S, W):
    w_child_adult_dict[w].append(s)

max_cnt = 0
adult_history = 0
children_history = 0
for thresh in W_sorted_unique:
    # 閾値の子供の数
    tmp_child_cnt = len([s for s in w_child_adult_dict[thresh] if s == "0"])

    # # 今までのこどもの数
    # tmp_cnt = children_history
    
    # # 全大人の数 - 今までの大人の数
    # tmp_cnt += adult_num - adult_history
    # max_cnt = max(max_cnt, tmp_cnt)
    # print(max_cnt)

    # この閾値で増えた子供を追加
    children_history += tmp_child_cnt
    
    # 今までの大人の数を記録する
    adult_history += len(w_child_adult_dict[thresh]) - tmp_child_cnt

    # 
    tmp_cnt = children_history
    tmp_cnt += adult_num - adult_history
    max_cnt = max(max_cnt, tmp_cnt)
    # print(max_cnt)

print(max(max_cnt, adult_num, child_num))
