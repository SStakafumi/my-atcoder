# 星座
m = int(input())

star = [list(map(int, input().split())) for _ in range(m)]
star.sort()
origin = star[0]
movedStar = [(s[0]-origin[0], s[1]-origin[1]) for s in star]

n = int(input())
picture = [list(map(int, input().split())) for _ in range(n)]
picture.sort()

ans = [0, 0]
for i, p in enumerate(picture):
    movedPicture = [(pic[0]-p[0], pic[1]-p[1]) for pic in picture[i:]]
    if set(movedStar) <= set(movedPicture):
        ans = p[0]-origin[0], p[1]-origin[1]
        print(*ans)
        break
