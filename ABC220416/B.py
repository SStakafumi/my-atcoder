A, B, K = map(int, input().split())
cnt = 0
while True:
    if A >= B:
        print(cnt)
        break
    A *= K
    cnt += 1
