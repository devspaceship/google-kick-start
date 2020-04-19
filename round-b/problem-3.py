class Agent:
    def __init__(self):
        self.w = 1
        self.h = 1

    def _normalize(self):
        self.w %= int(1e9)
        self.h %= int(1e9)
        self.w = self.w if self.w != 0 else int(1e9)
        self.h = self.h if self.h != 0 else int(1e9)

    def translate(self, dw, dh):
        self.w += dw
        self.h += dh
        self._normalize()


def decode(line: str):  # returns [dw, dh]
    mw = {'N': 0, 'S': 0, 'W': -1, 'E': 1}
    mh = {'N': -1, 'S': 1, 'W': 0, 'E': 0}
    dw, dh = 0, 0

    l = len(line)
    for i, c in enumerate(line):
        if c in 'NSWE':
            dw += mw[c]
            dh += mh[c]
        elif c in '23456789':
            stack = []
            match = i + 1
            for j in range(i + 1, l):
                lj = line[j]
                if lj == '(':
                    stack.append('(')
                elif lj == ')':
                    stack.pop()
                if len(stack) == 0:
                    match = j
                    break

            repeat = int(c)
            [_dw, _dh] = decode(line[i + 2:match])
            dw += _dw * repeat
            dh += _dh * repeat

            [_dw, _dh] = decode(line[match + 1:l])
            dw += _dw
            dh += _dh

            break

    return [dw, dh]


T = int(input())
for t in range(T):
    line = input()
    [dw, dh] = decode(line)
    agt = Agent()
    agt.translate(dw, dh)
    print("Case #{}: {} {}".format(t + 1, agt.w, agt.h))
