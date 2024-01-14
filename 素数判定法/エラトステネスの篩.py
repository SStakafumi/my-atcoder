# その①
def get_prime_list_ex(limit):
    '''エラトステネスの篩(limitまでの素数リストを返す)'''
    if limit < 2:
        return []

    # primep[n]==Trueのとき、(2 * n) + 1 が素数とする
    primep = [True] * ((limit - 1) // 2 + 1)

    primep[0] = False

    # 少しややこしく見えるが、やっていることは同じ
    # f.e. primep[3]==True(=7)の場合、
    # primep[10](=21), primep[17](=35)...と
    # 素数から除外されていくことになる
    for n in range(1, int((limit ** 0.5) - 1) // 2 + 1):
        if primep[n] == True:
            p = 2 * n + 1
            for i in range(n + p, len(primep), p):
                primep[i] = False

    # 2だけはしょうがないので最後に追加する
    return [2] + [2 * p + 1 for p in range(len(primep)) if primep[p] == True]


# # その② その①とそんなに変わらない


# def Eratosthenes(n):
#     """n以下の素数をエラトステネスの篩によって求める.リストをかえす"""
#     prime = []
#     limit = n**0.5
#     data = [i + 1 for i in range(1, n)]
#     while True:
#         p = data[0]
#         if limit <= p:
#             return prime + data
#         prime.append(p)
#         data = [e for e in data if e % p != 0]
