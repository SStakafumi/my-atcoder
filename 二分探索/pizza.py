# import bisect

# circle_length = int(input())
# store_num = int(input())
# order_num = int(input())
# store_poses = [0] + [int(input()) for _ in range(store_num-1)] + [circle_length]
# customer_poses = [int(input()) for _ in range(order_num)]

# ans = 0

# store_poses = sorted(store_poses)

# for customer_pos in customer_poses:
#     left_dis = customer_pos - store_poses[bisect.bisect_right(store_poses, customer_pos)-1]
#     right_dis = store_poses[bisect.bisect_left(store_poses, customer_pos)] - customer_pos
#     ans += min(left_dis, right_dis)

# print(ans)

from bisect import bisect

d = int(input())  # 全長
n = int(input())  # 店舗の個数
m = int(input())  # 注文の個数
storePos = [0] + [int(input()) for _ in range(n-1)]  # 店の位置のリスト
delPos = [int(input()) for _ in range(m)]  # 配達先の位置のリスト

storePos.sort()


def distance(i: int, l: list):
    index = bisect(l, i)
    if index == len(l):  # 配達位置が全ピザ店より時計回りでもっとも奥にあったら本店と比較
        dis = min(i-l[index-1], d-i)
    else:
        dis = min(i-l[index-1], l[index]-i)
    return dis


ans = 0
for i in delPos:
    ans += distance(i, storePos)

print(ans)