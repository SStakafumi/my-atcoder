from collections import deque

N, M = map(int, input().split())
S = list(map(str, input().split()))
T = deque(map(str, input().split()))

for i in range(N):
    if T == deque([]):
        print("No")
    elif S[i] != T[0]:
        print("No")
    else:
        print("Yes")
        T.popleft()
