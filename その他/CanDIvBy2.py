N = int(input())
A = list(map(int, input().split()))
cnt = 0
canDiv = True

while True:
    for a in A:
        if a % 2 == 1:
            canDiv = False

    if canDiv == False:
        break
    else:
        for i in range(N):
            A[i] = A[i] / 2
        cnt += 1

print(cnt)
