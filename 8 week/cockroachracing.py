from sys import stdin
import itertools
import operator
import functools

stdin = open('input.txt', 'r', encoding='utf8')
# K - количество тараканов
# N - количество болельщиков (ставок)
# Ключи тестирования
f_print = True
f_data = True
f_dbg = False


# Проверка данных (поскольку итераторы перечисляются единожды
if f_print:
    # Чтение входных данных в итератор map, где 1 элемент - "permutations" (все возможные итоги забегов из K тараканов);
    # 2 - входные данные из файла (по 2 ставки болельщиков)
    vb = functools.reduce(
        lambda K, N:
        [itertools.permutations(
            map(
                str, range(1, K + 1)
            )
        ), map(
            lambda tmp:
            stdin.readline().split(),
            range(N)
        )
        ], map(int, stdin.readline().split())
    )
    # vb = map(
    #     lambda kn:
    #     list(
    #         map(
    #             lambda tmp:
    #             stdin.readline().split(),
    #             range(kn[1])
    #         )
    #     ) if kn[0]
    #     else itertools.permutations(
    #         map(str, range(1, kn[1] + 1))),
    #     enumerate(
    #         map(
    #             int, stdin.readline().split()
    #         )
    #     )
    # )
    if f_data:
        functools.reduce(
            lambda v_test, b_test: print('Cписок вариантов и ставок:', *v_test, '', *b_test, sep='\n'), vb)
    elif f_dbg:
        v_test = next(vb)
        b_test = next(vb)
        res_test = list(filter(
            lambda variant: all(
                map(
                    lambda bet: operator.xor(variant.index(bet[0]) < variant.index(bet[1]),
                                             variant.index(bet[2]) < variant.index(bet[3])),
                    b_test
                )
            ), v_test
        ))
    else:  # Комбинация двух предыдущих отлаженных if-ов
        res_test = functools.reduce(
            lambda v_test, b_test:
            next(
                filter(
                    lambda variant:
                    all(
                        map(
                            lambda bet:
                            operator.xor(variant.index(bet[0]) < variant.index(bet[1]),
                                         variant.index(bet[2]) < variant.index(bet[3])),
                            b_test
                        )
                    ),
                    v_test
                ), 0
            ),
            vb
        )
else:
    print(*functools.reduce(
        lambda v_test, b_test:
        next(
            filter(
                lambda variant:
                all(
                    map(
                        lambda bet:
                        operator.xor(variant.index(bet[0]) < variant.index(bet[1]),
                                     variant.index(bet[2]) < variant.index(bet[3])),
                        b_test
                    )
                ),
                v_test
            ), [0]
        ), functools.reduce(lambda k, n: [itertools.permutations(
            map(
                str, range(1, k + 1)
            )
        ), list(map(
            lambda tmp:
            stdin.readline().split(),
            range(n)
        ))
        ], map(int, stdin.readline().split()))
    ))

eee = 0
