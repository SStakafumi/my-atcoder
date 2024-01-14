from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# dist型においてvalueの型を予め決めることができる
# 例えばint() は 0 を返すので
# from collections import defaultdict
# d = defaultdict(int)

# for key in val_str:
#     d[key] += 1
# keyがあるかないか気にせずこんなことができる
# また存在しないkeyを参照することもできる

m = defaultdict(list)
for i in range(N):
    # defaultdictでkey:[]の状態になっているのでいきなりappendしてもOK
    m[A[i]].append(i+1)

for _ in range(Q):
    x, k = map(int, input().split())
    if k <= len(m[x]):
        print(m[x][k-1])
    else:
        print(-1)


# 自分の回答
# import sys
# def input(): return sys.stdin.readline().rstrip()


# N, Q = map(int, input().split())
# A = list(map(str, input().split()))
# X = []
# K = []
# for i in range(Q):
#     x, k = map(int, input().split())
#     X.append(x)
#     K.append(k)

# d = {}
# for i in range(N):
#     key = A[i]
#     if key not in d:
#         d[key] = []
#     d[key].append(i)

# for x, k in zip(X, K):
#     if str(x) not in d.keys():
#         print(-1)
#     else:
#         if k <= len(d[str(x)]):
#             print(d[str(x)][k-1]+1)
#         else:
#             print(-1)
