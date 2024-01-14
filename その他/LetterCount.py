alpha = 'abcdefghijklmnopqrstuvwxyz'
text = ''

while True:
    try:
        text += input().lower()
    except EOFError:
        break  # EORErrorはinput時にctrl+z+Enterで出せる

for a in alpha:
    print('{} : {}'.format(a, text.count(a)))
