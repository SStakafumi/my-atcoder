while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    A = [[""] * W  for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                A[i][j] = "#"
            else:
                A[i][j] = "."
    for i in range(len(A)):
        b = "".join(A[i])
        print(b)
    print()



