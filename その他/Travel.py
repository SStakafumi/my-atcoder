def canTravel(t_1, x_1, y_1, t_2, x_2, y_2):
    time = t_2 - t_1
    dis = abs(x_2 - x_1) + abs(y_2 - y_1)
    if time - dis >= 0 and (time - dis) % 2 == 0:
        return True
    else:
        return False


N = int(input())
t0 = x0 = y0 = 0

for i in range(N):
    t, x, y = map(int, input().split())
    if not canTravel(t0, x0, y0, t, x, y):
        print("No")
        break
    t0, x0, y0 = t, x, y
else:
    print("Yes")
