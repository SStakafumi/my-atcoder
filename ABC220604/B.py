N = int(input())

graph = [[0]*31 for _ in range(31)]

for i in range(31):
    for j in range(31):
        if i == 0:
            graph[i][j] = 1
            break
        elif j == 0 or i == j:
            graph[i][j] = 1
        else:
            graph[i][j] = graph[i-1][j-1] + graph[i-1][j]

for i in range(N):
    print(' '.join(list(map(str, graph[i][:i+1]))))
