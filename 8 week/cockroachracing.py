from sys import stdin
import itertools
import operator
import functools
stdin = open('input.txt', 'r', encoding='utf8')
# K - количество тараканов
# N - количество болельщиков (ставок)
# K, N = tuple(map(int, stdin.readline().split()))
kn = map(int, stdin.readline().split())
# Варианты итогов забегов
variants = list(itertools.permutations(map(str, range(1, next(kn) + 1))))
# Ставки
bets = list(map(lambda tmp: stdin.readline().split(), range(next(kn))))
# Отбор забегов, удовлетворящих условию "сыграла только одна из ставок" (XOR)
good_variants = []
good_variants2 = list(
    filter(
        lambda varics: all(
            map(
                lambda y: operator.xor(varics.index(y[0]) < varics.index(y[1]),
                                       varics.index(y[2]) < varics.index(y[3])),
                bets
            )
        ),
        variants)
)
for variant in variants:
    anybet = True
    for bet in bets:
        anybet &= operator.xor(variant.index(bet[0]) < variant.index(bet[1]),
                               variant.index(bet[2]) < variant.index(bet[3]))
    if anybet:
        good_variants.append(variant)
if good_variants:
    print(*good_variants[0])
else:
    print(0)
eee = 0
