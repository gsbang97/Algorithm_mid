import string

def isAlpha(a):
    if a in string.ascii_letters:
        return True
    return False
    
def palindrome(s):
    queue = list()
    stack = list()
    for x in s:
        if isAlpha(x):
            queue.append(x.lower())
            stack.append(x.lower())
    while queue:
        if queue.pop(0) != stack.pop():
            return False
    if stack:
        return False
    return True
print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam"))
print(palindrome("Madam, I am Adam"))
        
    
    