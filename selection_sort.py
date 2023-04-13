def sort(list):
  result = []
  for _ in range(len(list)):
    m = list[0]
    for x in list[1:]:
      if x < m:
        m = x
    list.remove(m)
    result.append(m)
  return result


import random
q = [random.randint(1, 1000) for _ in range(10)]
print(q)
print(sort(q))
