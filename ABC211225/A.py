X, Y = map(int, input().split())
cnt = 0

while True:
    if X + cnt * 10 < Y:
        cnt += 1
    else:
        break

print(cnt)
