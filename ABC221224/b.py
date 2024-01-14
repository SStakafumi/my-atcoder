N = int(input())
A = list(map(int, input().split()))
A = [0] + A
Q = int(input())
queries = []

for i, q in enumerate(range(Q)):
    tmp_q = list(map(int, input().split()))
    if tmp_q[0] == 1:
        A[tmp_q[1]] = tmp_q[2]
    else:
        print(A[tmp_q[1]])