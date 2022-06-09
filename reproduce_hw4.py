print('--- task: reproduce dice experiment in python ---\n')

import matplotlib.pyplot as plt

double_standard = {}
for i in range(1, 7):
    for j in range(1, 7):
        s = i + j
        if s in double_standard:
            double_standard[s] += 1
        else:
            double_standard[s] = 1
print(double_standard)

dice = []
for i in range(2, 12):
    for j in range(i, 12):
        for k in range(j, 12):
            for l in range(k, 12):
                for m in range(l, 12):
                    dice.append([1, i, j, k, l, m])
print(dice)
for d1 in dice:
    for d2 in dice:
        dict = {}
        for i in d1:
            for j in d2:
                s = i + j
                if s in dict:
                    dict[s] += 1
                else:
                    dict[s] = 1
        if dict == double_standard:
            print(d1, " and ", d2)

print('\n loading the plot...')

plt.scatter(double_standard.keys(), double_standard.values())
plt.show()
