from sys import stdin
import math
print(2,
      *filter(
        lambda el_in: all(
          map(
            lambda divider: el_in % divider != 0,
            range(2, int(math.sqrt(el_in)) + 2)
              )
                          ),
        range(3, int(stdin.readline()) + 1)
              )
      )
