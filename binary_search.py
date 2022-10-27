def binary_search(list, cmp,size):
    length = len(list)//2
    print(length,cmp,list[length],size)
    if cmp == list[length]:
        return length+size
    elif cmp > list[length]:
        return binary_search(list[length+1:],cmp,size+length)
    else:
        return binary_search(list[:length],cmp,size)
l = [x for x in range(1000)]
print(binary_search(l,33,0))
    