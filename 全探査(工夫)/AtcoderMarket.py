N = int(input())
A = [0]*N
B = [0]*N

for n in range(N):
    A[n], B[n] = map(int, input().split())

sA = sorted(A)
sB = sorted(B)

inPoint = sA[len(A)//2]
outPoint = sB[len(B)//2]

dis = 0

for a, b in zip(A, B):
    dis += abs(a-inPoint) + abs(b-outPoint) + (b-a)

print(dis)
