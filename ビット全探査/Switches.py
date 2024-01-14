N, M = map(int, input().split())
lamps = [list(map(lambda x: int(x) - 1, input().split()))[1:]
         for _ in range(M)]  # [1:]とすることでkは無視
p = list(map(int, input().split()))
ans = 0

# bit全探索(スイッチの入れ方を全探索する)
for i in range(1 << N):
    for r in range(M):  # 全てのランプがついてるかチェック
        print(i, r)
        on_sum = 0  # ランプrにおいて、onのスイッチの数
        for j in range(N):  # スイッチのj番目について
            if i >> j & 1 and j in lamps[r]:
                on_sum += 1  # onでスイッチjがランプrに繋がってたらonSum += 1
        if on_sum % 2 != p[r]:  # on_off check
            break  # 一つでもoffなら次のビットに
    else:
        ans += 1
print(ans)
