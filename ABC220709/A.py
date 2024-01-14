N, M, X, T, D = map(int, input().split())

if M >= X:
    print(T)
else:
    ans = T - D*(X-M)
    print(ans)
