N = int(input())
snnms = {}
for i_s in range(N):
    wrds = input().split()
    snnms[wrds[0]] = wrds[1]
    snnms[wrds[1]] = wrds[0]
print(snnms[input()])
