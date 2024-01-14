A, B, C, X, Y = map(int, input().split())
minPrice = 1000000000

for k in range(max(X, Y) + 1):
    price = A * max(X - k, 0) + B * max(Y - k, 0) + 2 * C * k
    if price < minPrice:
        minPrice = price

print(minPrice)
