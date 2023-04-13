def mergy_sort(slist):
    length = len(slist)
    if length <= 1: # 최소단위까지
        return slist
    left = mergy_sort(slist[:length//2])
    right = mergy_sort(slist[length//2:])

    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left is not None:
        result += left
    if right is not None:
        result = result + right
    return result

import random

l = [random.randint(1,100) for _ in range(10)]
print(l)
print(mergy_sort(l))