fin = open('input.txt', 'r', encoding='utf8')
school_bal = [[0 for i in range(2)] for j in range(100)]
for pupil in fin:
    pupil = list(pupil.strip().split())
    pupil[-2::] = list(map(int, pupil[-2::]))
    school_bal[pupil[-2]][0] = pupil[-2]
    school_bal[pupil[-2]][1] += 1
school_bal.sort(key=lambda sch: -sch[-1])
K = 1
while school_bal[K][1] == school_bal[K - 1][1]:
    K += 1
schools = []
for i in range(K):
    schools.append(school_bal[i][0])
schools.sort()
print(*schools)
