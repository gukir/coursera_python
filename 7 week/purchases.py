fin = open('input.txt', 'r', encoding='utf8')
buyers = dict()
for i_line in fin:
    prsn, prchs, cnt = i_line.split()
    cnt = int(cnt)
    buyers[prsn] = buyers.get(prsn, dict())
    buyers[prsn][prchs] = buyers[prsn].get(prchs, 0) + cnt
for buyer in sorted(buyers):
    print(buyer, ':', sep='')
    for purchase in sorted(buyers[buyer]):
        print(purchase, buyers[buyer][purchase])
