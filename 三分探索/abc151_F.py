N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

def get_radius(*center):
    r = 0
    for i in range(N):
        r = max(r, get_distance(*points[i], *center))
    return r

low_x = 0
high_x = 1000
loop_num = 100 

def calc_y(x):
    low_y = 0
    high_y = 1000
    cnt = 0
    while cnt < loop_num:
        cnt += 1
        c1 = (low_y * 2 + high_y) / 3
        c2 = (low_y + high_y * 2) / 3

        if get_radius(x, c1) > get_radius(x, c2):
            low_y = c1
        else:
            high_y  = c2

    return low_y

cnt = 0
while cnt < loop_num:
    cnt += 1
    c1 = (low_x * 2 + high_x) / 3
    c2 = (low_x + high_x * 2) / 3
    if get_radius(c1, calc_y(c1)) > get_radius(c2, calc_y(c2)):
        low_x = c1
    else:
        high_x = c2

print(get_radius(low_x, calc_y(low_x)))   