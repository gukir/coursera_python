busst = list(map(int, input().split()))
stations = set()
for i_b in range(len(busst)//2):
    route = set(range(min(busst[2 * i_b: 2 * i_b + 2]),
                      max(busst[2 * i_b: 2 * i_b + 2]) + 1))
    if not i_b:
        stations = route
    else:
        stations.intersection_update(route)
print(stations.__len__())
