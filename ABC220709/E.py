N = int(input())
all_list = []

for i in range(N):
    m = int(input())
    tmp_num = 1
    for _ in range(m):
        p, e = map(int, input().split())
        tmp_num *= p**e
    all_list.append(tmp_num)


def lcm(list_l):
    greatest = max(list_l)
    i = 1
    while True:
        for j in list_l:
            if (greatest * i) % j != 0:
                i += 1
                break
        else:
            return greatest * i

ans = set()   

for i in range(N):
    tmp_list = all_list.copy()
    tmp_list[i] = 1
    ans.add(lcm(tmp_list))

print(len(ans))
    