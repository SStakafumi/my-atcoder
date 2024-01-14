H, W = map(int, input().split())

ans = 0
for i in range(H):
    s = input()
    ans += s.count("#")

print(ans)