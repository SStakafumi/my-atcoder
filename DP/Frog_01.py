# myAns
n = int(input())
h = list(map(int, input().split()))

dp = [0, abs(h[0]-h[1])]
for i in range(2, n):
    # ある足場までの最小値をDPに格納しておく
    # 足場Kに行くにはK-2かK-1かのどちらかからしか行けないのだから
    #   足場Kの最小値はK-1, K-2の最小値のみで決定できることに注意
    dp += [min(dp[-2]+abs(h[i]-h[i-2]), dp[-1]+abs(h[i]-h[i-1]))]

print(dp[-1])
