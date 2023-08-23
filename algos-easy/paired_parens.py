# Paired Parentheses

# Write a function, paired_parens, that takes in a string as an argument. 
# The function should return a boolean indicating whether or not the string has well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.


def paired_parens(string):
  # create a stack 
  stack = []
  # iterate through the string
  for char in string:
    
    # if current char is opening bracket
    if char == "(":
      # append it to the stack
      stack.append(char)
      # if the current char is closing backet and if stack has nothing in it
    elif char == ")":
      if len(stack) == 0:
        # return false right away
        return False
      # if last element is opening bracket
      elif stack[-1] == "(":
        # pop the opening bracket from the stack
        stack.pop()
  # if the stack has nothing in it, that means all brackets were paired so we return True, else False
  if len(stack) == 0:
    return True
  else:
    return False







# TEST CASES
print(paired_parens("(david)((abby))")) # -> True
print(paired_parens("()rose(jeff")) # -> False
print(paired_parens(")(")) # -> False
print(paired_parens("()")) # -> True
print(paired_parens("(((potato())))")) # -> True
print(paired_parens("(())(water)()")) # -> True
