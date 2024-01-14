n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

C = []
c = 0
for i in range(n):
    for j in range(l):
        for k in range(m):
            c += A[i][k] * B[k][j]
        C.append(c)
        c = 0
    C = list(map(str, C))
    ans = " ".join(C)
    C = []
    print(ans)
