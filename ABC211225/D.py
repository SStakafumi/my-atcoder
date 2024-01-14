N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(1, N-i+1):
        if sum(A[i:i+j]) == K:
            cnt += 1

print(cnt)
