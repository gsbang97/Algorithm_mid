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


q = []
import random
for x in range(10):
  q.append(random.randint(1, 1000))
print(q)
print(sort(q))
