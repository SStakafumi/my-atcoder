# ナップザックDP(同じものは2回以上選ばない)
def Knapsak(costList, valueList, costLimit):
    costListLen = len(costList)
    dp = [[0]*(costLimit+1) for _ in range(costListLen)]

    # # １つ目の対象を選択するか・・・①
    # for j in range(costLimit+1):
    #     if j >= costList[0]:
    #         dp[0][j] = valueList[0]

    # # 2つ目以降の対象を選択するか・・・②
    # for i in range(1, costListLen):
    #     for j in range(costLimit+1):
    #         # 選択しない時の最大価値
    #         notChoiceValue = dp[i-1][j]
    #         if j < costList[i]:  # カロリーオーバー
    #             dp[i][j] = notChoiceValue
    #         else:
    #             choiceValue = dp[i-1][j-costList[i]] + valueList[i]
    #             dp[i][j] = max(notChoiceValue, choiceValue)

    # ①＋② (こっちのほうだと重複ありでも解ける)
    for i in range(costListLen):
        for j in range(costLimit+1):
            # 選択しない時の最大価値
            notChoiceValue = dp[i-1][j]
            if j < costList[i]:  # カロリーオーバー
                dp[i][j] = notChoiceValue
            else:
                # 重複ありのナップザックだとchoiceValue_2を追加
                choiceValue_1 = dp[i-1][j-costList[i]] + valueList[i]
                # choiceValue_2 = dp[i][j-costList[i]] + valueList[i]
                dp[i][j] = max(notChoiceValue, choiceValue_1)  # choiceValue_2)

    return dp[costListLen-1][costLimit]


# Input

'''
Input例
N W     品数, コスト制限(重さとか)
v1 w1   価値, コスト
v2 w2
:
vN wN
'''

N, costLimit = map(int, input().split())
valueList = []
costList = []
for n in range(N):
    v, w = map(int, input().split())
    valueList.append(v)
    costList.append(w)

# costList = [8, 10, 7, 6, 7]  # コスト(これに制約がかかる)
# valueList = [120, 150, 140, 110, 100]  # 価値(この組み合わせで価値を最大化したい)
ans = Knapsak(costList, valueList, costLimit)
print(ans)
