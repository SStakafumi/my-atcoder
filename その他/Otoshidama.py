def solve(N, Y):
    leftMoney = Y - 1000 * N
    if leftMoney < 0:
        return -1, -1, -1
    else:
        for j in range(leftMoney // 4000 + 1):
            if (leftMoney - 4000 * j) % 9000 == 0:
                x = (leftMoney - 4000 * j) // 9000  # 商は整数で帰ってくる
                if x + j <= N:
                    return x, j, N - x - j
    return -1, -1, -1


print(*solve(*map(int, input().split())))


######### 別解 ###############
'''
n, y = map(int, input().split())
for i in range(n + 1):
    for j in range(n - i + 1):
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print(i, j, n - i - j)
            exit()
print("-1 -1 -1")
'''

######## 別解 ###############

'''
def solve(n, y):
    tmp1000 = n * 1000
    if tmp1000 > y:
        return -1, -1, -1
    diff = y - tmp1000
    for y in range(diff // 4000 + 1):
        tmp5000 = y * 4000
        if diff - tmp5000 < 0:
            break
        if (diff - tmp5000) % 9000 == 0:
            x = (diff - tmp5000) // 9000
            if x >= 0 and x + y <= n:
                return x, y, n - x - y
    return -1, -1, -1

print(*solve(*map(int, input().split())))

'''
