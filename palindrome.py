import string

def isAlpha(a):
    return a in string.ascii_letters
    
def palindrome(s):
    queue = []
    stack = []
    for x in s:
        if isAlpha(x):
            queue.append(x.lower())
            stack.append(x.lower())
    while queue:
        if queue.pop(0) != stack.pop():
            return False
    return not stack
print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam"))
print(palindrome("Madam, I am Adam"))
        
    
    