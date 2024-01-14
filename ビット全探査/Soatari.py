# TLE?

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

for m_tmp in m:
    for i in range(2**q):
        tmp_sum = 0
        for j in range(q):
            if ((i >> j) & 1):
                tmp_sum += A[j]
        if tmp_sum == m_tmp:
            print('yes')
            break
    else:
        print('no')
