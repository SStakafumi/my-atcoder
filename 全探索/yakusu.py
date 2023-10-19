n = int(input())

ans = 0
for i in range(1, n+1):
    if i%2 == 0:
        continue
    cnt = 0
    for j in range(1, i+1):
        if j**2 > i:
            break
        elif j**2 == i:
            cnt += 1
        elif i%j == 0:
            cnt += 2
    if cnt == 8:
        ans += 1

print(ans)