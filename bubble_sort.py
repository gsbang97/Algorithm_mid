def bubble(list):
    length = len(list)
    for i in range(length):
        for j in range(i,length):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
import random
l = [random.randint(1,100) for _ in range(100)]
bubble(l)

print(l)