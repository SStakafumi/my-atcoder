X, A, D, N = map(int, input().split())
t1 = A
t2 = A + D * (N-1)
tips = sorted([t1, t2])

if D == 0:
    ans = abs(X-A)
elif tips[0]-X >= abs(D):
    ans = tips[0] - X
elif X-tips[1] >= abs(D):
    ans = X - tips[1]
else:
    AmodD = A % D
    XmodD = X % D
    ans = min(abs(AmodD-XmodD), abs(D)-abs(AmodD-XmodD))

print(ans)
