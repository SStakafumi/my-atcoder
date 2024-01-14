N = int(input())
orgN = N

i = 2
ans = []
dicAns = {}

for i in range(2, int(N**(1/2)+1)):
    if N % i != 0:
        # 割れなかったら何もしない
        continue

    ex = 0  # 指数

    while N % i == 0:
        # 割れる限り割り続ける
        ex += 1
        N //= i
        ans.append(i)
    dicAns[i] = ex

    i += 1

if N != 1:
    # 最後に余った数の処理
    ans.append(N)
    dicAns[N] = 1


# N = 12 の時
# print(" ".join(map(str, ans)))  # 2 2 3
print("{0}:".format(orgN), *ans)  # 12: 2 2 3
# for item in dicAns:
#     print("{} {}".format(item, dicAns[item]))
#     # 2 1
#     # 3 2
#     # 7 1
