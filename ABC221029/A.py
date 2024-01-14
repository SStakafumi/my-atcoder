import numpy as np

N = int(input())
H = list(map(int, input().split()))
n_h = np.array(H)

print(np.argsort(-n_h)[0]+1)
