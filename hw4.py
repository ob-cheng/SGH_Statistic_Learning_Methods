
import matplotlib.pyplot as plt
standard = {}
for i in range (1,7):
    for j in range (1,7):
        s = i+j
        if s in standard:
            standard[s]+=1
        else:
            standard[s] = 1
print(standard)
plt.scatter(standard.keys(),standard.values())
plt.show()
all_dice = []
for i in range (2,12):
    for j in range(i,12):
        for k in range(j, 12):
            for l in range(k, 12):
                for m in range(l, 12):
                    all_dice.append([1,i,j,k,l,m])
print(all_dice)
for d1 in all_dice:
    for d2 in all_dice:
        all_dict = {}
        for i in d1:
            for j in d2:
                s = i + j
                if s in all_dict:
                    all_dict[s] += 1
                else:
                    all_dict[s] = 1
        if (all_dict == standard):
            print(d1," n ", d2)
