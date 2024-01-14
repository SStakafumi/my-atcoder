N = int(input())

first_s = ['H', 'D', 'C', 'S']
second_s = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

flag = True
all_str = set()

for i in range(N):
    if flag != True:
        break

    s = input()
    f_str = s[0]
    s_str = s[1]

    if f_str not in first_s:
        flag = False
    if s_str not in second_s:
        flag = False

    all_str.add(s)

if flag and len(all_str) == N:
    print('Yes')
else:
    print('No')
