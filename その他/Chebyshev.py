def Distance(X, Y, p):
    s = 0
    for x, y in zip(X, Y):
        s += abs(x-y)**p
    print(s**(1/p))


n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

for p in range(1, 4):
    Distance(X, Y, p)
print(max(abs(x-y) for x, y in zip(X, Y)))
