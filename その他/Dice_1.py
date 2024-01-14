d1, d2, d3, d4, d5, d6 = map(str, input().split())

top = d1
bottom = d6
s = d2
n = d5
w = d4
e = d3

order = str(input())
for o in order:
    if o == "S":
        [top, n, bottom, s] = [n, bottom, s, top]
    elif o == "N":
        [top, n, bottom, s] = [s, top, n, bottom]
    elif o == "W":
        [top, e, bottom, w] = [e, bottom, w, top]
    elif o == "E":
        [top, e, bottom, w] = [w, top, e, bottom]
    else:
        break

print(top)
