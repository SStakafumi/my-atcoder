def find_max_dp(num_list, limit):
    list_len = len(num_list)
    dp_table = [[0 for _ in range(limit + 1)] for _ in range(list_len)]

    # 1番目のカード(これいるか？)
    """ for j in range(limit + 1):
        if num_list[0] <= j:
            dp_table[0][j] = list[0]  # 1番目のカードを追加 """

    # 2番目以降のカード
    for i in range(list_len):
        for j in range(limit + 1):
            tmp_not_choice = dp_table[i-1][j]
            if num_list[i] > j:  # コストオーバーのとき
                dp_table[i][j] = tmp_not_choice  # 選ばない
            else:  # まだコストが余ってるとき
                tmp_choice = dp_table[i-1][j - num_list[i]] + num_list[i]
                dp_table[i][j] = max(tmp_choice, tmp_not_choice)

    return dp_table[list_len - 1][limit]


list = [4, 8, 6]
print(find_max_dp(list, 10))
