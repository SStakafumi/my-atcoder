from itertools import accumulate
N, Q = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
MOD = 10**9+7

D = [0]
for i in range(len(A)-1):
    d = pow(A[i], A[i+1], MOD)
    D.append(d)
acc = list(accumulate(D))

C.insert(0, 1)
C.append(1)
ans = 0
for q in range(len(C)-1):
    ans += abs(acc[C[q+1]-1]-acc[C[q]-1]) % MOD

print(ans % MOD)
