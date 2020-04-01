N = int(input())
people = set()
tree = dict()
for i_n in range(N - 1):
    chld, fthr = input().split()
    tree[chld] = fthr
ans = []
level = -1
level_search_next = []
while len(ans) < N:
    level_search = level_search_next
    level_search_next = []
    level += 1
    if not level_search:  # Root search
        for chld in tree:
            if tree[chld] not in tree:
                ans.append((tree[chld], level))
                level_search_next = [tree[chld]]
                break
    else:
        for chld in tree:
            if tree[chld] in level_search:
                level_search_next.append(chld)
                ans.append((chld, level))
for elem in sorted(ans):
    print(elem[0], elem[1])
