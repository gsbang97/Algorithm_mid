def sort(list):
  length = len(list)

  for i in range(1, length):
    j = i - 1
    tmp = list[i]

    while (j >= 0) and (tmp < list[j]):
      print(list, list[i], list[j], i, j)
      list[j + 1] = list[j]
      j -= 1
    list[j + 1] = tmp


l = list(range(10))
import random

random.shuffle(l)

print(l)
sort(l)
print(l)
