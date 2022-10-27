def bubble(list):
    length = len(list)
    for i in range(length):
        for j in range(i,length):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
import random
l = list()
for x in range(100):
    l.append(random.randint(1,100))
bubble(l)

print(l)