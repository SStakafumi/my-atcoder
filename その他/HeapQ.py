import heapq

a = [5, 2, 1, 3, 4, 2]

heapq.heapify(a)  # リストを優先度付きキューに変換(最初にこれが必要)
print(a)
# [1, 2, 2, 3, 4, 5]

v = heapq.heappop(a)  # 最小値の取り出し
print(v)
# 1
print(a)
# [2, 2, 3, 4, 5]

v = heapq.heappush(a, 3)  # 優先度付きキューに要素を挿入
print(a)
# [2, 2, 3, 3, 4, 5]
