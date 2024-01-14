N = int(input())

i = 1
ans = []
while i*i <= N:
    if N % i == 0:
        ans.append(i)
        if i*i != N:
            ans.append(N // i)
    i += 1
ans.sort()
print(" ".join(map(str, ans)))
# 1 2 3 4 6 12 (N = 12)
