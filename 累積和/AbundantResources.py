N = int(input())
A = [0] + list(map(int, input().split()))

S = [0] * (N+2)
S[0] = 1

for i in range(1, N+1):
    S[i+1] = S[i] + A[i]

for k in range(1, N+1):
    ans = 0
    for i in range(1, N - k + 2):
        # if i + k - 1 > N:
        #     break
        ans = max(ans, S[i+k]-S[i])

    print(ans)
