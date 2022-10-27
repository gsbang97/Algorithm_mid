def find_width(w,h):
    if(w>h): w,h = h,w
    if(h%w == 0): return w
    print(w)
    return find_width(w,h%w)
    
width, height = map(int,input("농장의 가로길이 세로길이:").split())
length = find_width(width, height)
print("한 변의 길이:",length)
print("밭의 개수:", (width*height)//(length**2))


