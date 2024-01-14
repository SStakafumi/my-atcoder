N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

indexList = [i for i, v in enumerate(A) if v == max(A)]

flag = True

for b in B:
    b -= 1
    if b in indexList:
        flag = False
        break

if not flag:
    print('Yes')
else:
    print('No')


# 2
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# maxA = max(a)
# flag = False

# for i in range(k):
#     if a[b[i]-1] == maxA:
#         flag = True
#         break

# if flag:
#     print("Yes")
# else:
#     print("No")
