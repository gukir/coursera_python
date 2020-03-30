dist = list(map(int, input().split()))
dist.sort()
price = list(map(int, input().split()))
price.sort(reverse=True)
fullsum = 0
for i in range(len(dist)):
    fullsum += price[i] * dist[i]
print(fullsum)
