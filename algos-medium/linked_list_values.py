
# Linked List Values

# Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
# The function should return a list containing all values of the nodes in the linked list.

# Do not edit Class
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  # list = []
  # curr = head
  # while(curr):
  #   list.append(curr.val)
  #   curr = curr.next
  # return list
  if head is None:
    return []
  return [head.val] + (linked_list_values(head.next))
  


# TEST CASES

# 1.
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]

2.
x = Node("x")
y = Node("y")
x.next = y
print(linked_list_values(x)) # -> [ 'x', 'y' ]

3.
q = Node("q")
print(linked_list_values(q)) # -> [ 'q' ]

4.
print(linked_list_values(None)) # -> [ ]
