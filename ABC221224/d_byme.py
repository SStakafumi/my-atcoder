import sys
S = input()

stack = []
in_box = set()

for i, s in enumerate(S):
    if s == '(':
        stack.append(set())
    elif s == ')':
        if len(stack)>=1:
            in_box -= stack[-1]
            stack.pop()
    else:
        if s in in_box:
            print('No')
            sys.exit()
        in_box.add(s)
        if len(stack) >= 1:
            stack[-1].add(s)
            
print('Yes')
        
        