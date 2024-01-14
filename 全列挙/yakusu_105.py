N = int(input())

allD = []

for n in range(1, N+1):
    cnt = 0
    for i in range(1, n+1):
        if i*i > n:
            break
        elif i*i == n:
            cnt -= 1/2
        elif n % (i) == 0:
            cnt += 1
    allD.append(cnt*2)

ans = 0
for i, k in enumerate(allD):
    if (i+1) % 2 == 1 and k == 8:
        ans += 1
print(ans)
