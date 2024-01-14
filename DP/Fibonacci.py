""" 
#自分の解法
n = int(input())
dp = [0]*(n+1)

if n == 0:
    print(1)
elif n == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
 """

# 再帰法(毎回１から計算しているから時間が指数関数的に大きくなっていく)
""" 
s = int(input())


def fib1(n):
    if n <= 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2) #何が何でも１から計算


print(fib1(s))
"""

# メモ化再帰
""" 
memo = [0] * (11)  # 結果をメモ（グローバル変数で宣言！）


def fib2(n):
    if n <= 1:
        return 1
    else:
        if memo[n] == 0:  # 一回計算すればここは通らないからいちいち計算せずにすむ
            memo[n] = fib2(n-1) + fib2(n-2)
        return memo[n]


print(fib2(6))
 """

# DP


def fib3(n):
    a = [1] * (n+1)  # a[0] = 1, a[1] = 1

    # a[2] 以降の導出
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]

    return a[n]


print(fib3(10))
