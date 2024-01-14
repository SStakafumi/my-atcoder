m, n = map(int, input().split())
mod = 10**9+7
# 勝手にmod計算してくれてとんでもなく大きい数にならないらしい
print(pow(m, n, mod))
