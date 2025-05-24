from itertools import permutations
import re
import timeit

# ---------- Initial Solution ----------
pieces = 'KQBbRrNN'
startPosition = {' '.join(p).lower() for p in permutations(pieces)
                if p.index('B') %2 != p.index('b') %2
                and (p.index('R') < p.index('K') < p.index('r')
                or p.index('r') < p.index('K') < p.index('R'))}
startPosition = sorted(startPosition)

def get_chess960_position(n):
    r = startPosition[n - 1]
    solution = '\n'.join((r, ' '.join(['p']*8), *[' '.join(['.']*8) for _ in range(4)], ' '.join(['P']*8), r.upper()))
    return solution + '\n'

# ---------- Additional Solution ----------
A = 'bbnnqrkr'
srp = set()
for r in permutations('bbknnqrr', 8):
    ib1, ib2 = r.index('b'), 7 - r[::-1].index('b')
    if (ib1 % 2) == (ib2 % 2):
        continue
    ir1, ir2, ik = r.index('r'), 7 - r[::-1].index('r'), r.index('k')
    if not ir1 < ik < ir2:
        continue
    srp.add(' '.join(r))
RP = sorted(srp)

def get_chess960_position_two(n):
    r = RP[n - 1]
    solution = '\n'.join((r, ' '.join(['p']*8), *[' '.join(['.']*8) for _ in range(4)], ' '.join(['P']*8), r.upper()))
    return solution + '\n'

# ---------- Additional Solution ----------
POS = sorted({s for p in permutations('BBKNNQRR') if re.match('(?=.*B(..)*B).*R.*K.*R', s := ''.join(p))})

def get_chess960_position_three(n):
    return '\n'.join(map(' '.join, [POS[n - 1].lower(), 'p' * 8, *['.' * 8] * 4, 'P' * 8, POS[n - 1]])) + '\n'

if __name__ == '__main__':
    # print(
    #     f'Naught Number Function: {timeit.timeit(lambda: get_chess960_position(1), number=100000000)}')
    # print(
    #     f'Naughty Number Two Function: {timeit.timeit(lambda: get_chess960_position_two(1), number=100000000)}')
    # print(
    #     f'Naughty Number Three Function: {timeit.timeit(lambda: get_chess960_position_three(1), number=100000000)}')
    
    # Naught Number Function: 190.12015170000086
    # Naughty Number Two Function: 188.7300488999972
    # Naughty Number Three Function: 266.73836189999565

    print(get_chess960_position(100))
    print(get_chess960_position_two(100))
    print(get_chess960_position_three(100))