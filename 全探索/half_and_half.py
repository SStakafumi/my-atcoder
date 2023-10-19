A, B, C, X, Y = list(map(int, input().split()))

ans = float('inf')

for i in range(max(X, Y)+1):
    # ABピザの枚数
    n_ab = i*2
    # Aピザの枚数
    n_a = max(0, X-i)
    # Bピザの枚数
    n_b = max(0, Y-i)

    ans = min(ans, A*n_a + B*n_b + C*n_ab)

print(ans)