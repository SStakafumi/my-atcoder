import bisect

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0
for t in T:
    if S[bisect.bisect_left(S, t)] == t:
        ans += 1

print(ans)

# # bisectを使わない場合
# _, S = input(), [*map(int, input().split())]
# _, T = input(), [*map(int, input().split())]

# def binary_search(S, t):
#     left, right = 0, len(S)
#     while left < right:
#         mid = (left + right) // 2
#         if S[mid] == t:
#             return True
#         if S[mid] > t:
#             right = mid
#         else:
#             left = mid + 1
#     return False

# print(sum(binary_search(S, t) for t in T))

