N, X = map(int, input().split())
P = list(map(int, input().split()))

for i, num in enumerate(P):
    if num == X:
        print(i+1)
        break
