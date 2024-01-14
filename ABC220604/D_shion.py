import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1:
    print("Yes")
    sys.exit()

sorted_A = sorted(A)
for i in range(K-1):
    tmp_sets_orig = set()
    tmp_sets_sorted = set()
    for j in range(i, N, K):
        tmp_sets_orig.add(A[j])
        tmp_sets_sorted.add(sorted_A[j])
    if tmp_sets_sorted != tmp_sets_orig:
        print("No")
        sys.exit()
print("Yes")
