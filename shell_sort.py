def sort(list):
  step_list = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
  step_list = [x for x in step_list if x < len(list)]
  for h in step_list[::-1]:
    print(h)
    for i in range(h, len(list)):
      j = i
      item = list[i]
      while j >= h and list[j - h] > item:
        list[j] = list[j - h]
        j -= h
      list[j] = item


l = [x for x in range(1000)]
import random

random.shuffle(l)

print(l)
sort(l)
print(l)
