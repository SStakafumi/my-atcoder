import sys
def input(): return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
A = list(map(int, input().split()))

# dp[i] = 山の石がi個の時、直後の番の人が勝つか？ : かつTrue, まけるFalse

dp = [None] * (K+1)

for i in range(K+1):
    if i < A[0]:
        dp[i] = False
    else:
        if i in A:
            dp[i] = True
        else:
            for a in A:
                if dp[i-a] == False:
                    dp[i] = True
                    break
                else:
                    dp[i] = False

if dp[K]:
    print("First")
else:
    print("Second")
