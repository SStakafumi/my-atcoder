N = int(input())
A = []

for i in range(N):
    a = list(''.join(input()))
    A.append(a)

flag = True

for i in range(N):
    if not flag:
        break
    for j in range(N):
        if i == j:
            continue
        else:
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    flag = False
                    break
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    flag = False
                    break
            else:
                if A[i][j] != 'D':
                    flag = False
                    break

if flag:
    print('correct')
else:
    print('incorrect')