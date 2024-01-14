import numpy as np

N = int(input())

Ss = np.array(list(map(int, input().split())))
print(*([Ss[0]] + list(np.diff(Ss))))
