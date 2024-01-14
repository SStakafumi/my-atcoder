import sys

S = input()
N = len(S)

stack = []
depth_set = set()

for i, s in enumerate(S):
    # print(stack, depth_set)
    if s == '(':
        stack.append(set())
    elif s == ')':
        if len(stack) >= 1:
            depth_set -= stack[-1]
            stack.pop()
    else:
        if s in depth_set:
            print('No')
            exit()
        depth_set.add(s)
        if len(stack) >= 1:
            stack[-1].add(s)

print('Yes')