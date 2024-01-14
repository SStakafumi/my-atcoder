class Dice():
    def __init__(self, sequence):
        self.sequence = sequence

    def move(self, code):
        return [self.sequence[int(idx)] for idx in str(code)]

    def roll(self, root):
        for d in root:
            if d == 'N':
                self.sequence = self.move(152304)
            elif d == 'E':
                self.sequence = self.move(310542)
            elif d == 'S':
                self.sequence = self.move(402351)
            elif d == 'W':
                self.sequence = self.move(215043)


seq = list(map(int, input().split()))
for _ in range(int(input())):
    a, b = map(int, input().split())
    for ops in ('', 'N', 'W', 'E', 'S', 'NN'):
        dice = Dice(seq)
        dice.roll(ops)
        for _ in range(4):
            dice.roll('NES')
            if dice.sequence[0] == a and dice.sequence[1] == b:
                print(dice.sequence[2])
