N = int(input())
N = N % (3600 * 24)
hours = int(N / 60 / 60)
minutes = int(N / 60) - hours * 60
seconds = N - hours * 60 * 60 - minutes * 60
print('%d:%02d:%02d' % (hours, minutes, seconds))
