import collections

N = int(input())
S = [input() for _ in range(N)]

placeList = [[0]*10 for _ in range(N)]

for i, s in enumerate(S):
    for j, k in enumerate(s):
        placeList[i][int(k)] = j

tmpList = [[0]*N for _ in range(10)]

for n, pl in enumerate(placeList):
    for i, num in enumerate(pl):
        tmpList[i][n] = num

maxTimes = [0]*10

for i, place in enumerate(tmpList):
    c = collections.Counter(place)
    if len(c) == N:
        maxTimes[i] = max(place)
    else:
        max_val = max(c.values())
        keys_of_max_val = [key for key in c if c[key] == max_val]
        maxTimes[i] = 10*(max_val-1) + max(keys_of_max_val)

print(min(maxTimes))


# # 2
# n = int(input())
# s = []

# for i in range(n):
#     s.append(input())  # s = ['1937458062', '8124690357', '2385760149']

# cnt = [[0 for _ in range(10)] for _ in range(10)]

# for i in range(n):
#     for j in range(10):
#         cnt[int(s[i][j])][j] = cnt[int(s[i][j])][j] + 1

# mx = [0 for _ in range(10)]

# for i in range(10):
#     for j in range(10):
#         mx[i] = max(mx[i], 10*(cnt[i][j]-1)+j)

# print(min(mx))
