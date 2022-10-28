# 괄호 여부 알고리즘 stack 응용

def isAlright(str):
  stack = []
  left_s = ['(', '{', '[']
  right_s = [')', '}', ']']
  for s in str:
    if s in left_s:
      stack.append(s)
    elif s in right_s:
      if stack:
        tmp = stack.pop()
        if left_s.index(tmp) != right_s.index(s):
          return False
      else:
        return False
  if stack:
    return False
  return True


print(isAlright("((())"))
print(isAlright("[{[}]}"))
print(isAlright("[({})asd]"))
