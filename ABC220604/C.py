import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

all = [[] for _ in range(K)]

for i, a in enumerate(A):
    bisect.insort_left(all[i % K], a)

flag = True

pre = 0
for i in range(N):
    next = all[i % K].pop(0)
    if pre <= next:
        pre = next
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
