# Depth First Values

# Write a function, depth_first_values, that takes in the root of a binary tree. 
# The function should return a list containing all values of the tree in depth-first order.

# Do not edit Class
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values(root, arr=[]):
  # iterative
  # result = []
  # stack = [root]
  # while stack:
  #   current = stack.pop()
  #   result.append(current.val)
  #   if current.right:
  #     stack.append(current.right)  
  #   if current.left:
  #     stack.append(current.left)
  # return result
  
  
  # recursive
  # curr = root
  # if curr:
  #   arr.append(curr.val)
  #   if curr.left: depth_first_values(curr.left, arr)
  #   if curr.right: depth_first_values(curr.right, arr)
  # return arr

# TEST CASE

# 1.
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
print(depth_first_values(a)) # EXPECTED OUTPUT  -> ['a', 'b', 'd', 'e', 'c', 'f']

# 2. 
# a = Node('a')
# depth_first_values(a) #   -> ['a']