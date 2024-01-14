N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i, a in enumerate(A):
    A[i] -= 1

for i, l in enumerate(L):
    L[i] -= 1

for l in L:
    # 一番右にいる
    if A[l] == N-1:
        continue
    # 右隣にいる
    elif A[l]+1 in A:
        continue
    else:
        A[l] += 1

for i, a in enumerate(A):
    A[i] += 1

A = map(str, A)
print(" ".join(A))
