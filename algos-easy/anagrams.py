# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
  char_list_1 = list(s1)
  char_list_2 = list(s2)
  
  char_count = {}
  
  for char in char_list_1:
      if char not in char_count:
          char_count[char] = 0
      char_count[char] += 1
      
  for char in char_list_2:
    if char not in char_count:
        return False
    char_count[char] -= 1

  
  for count in char_count.values():
        if count != 0:
            return False
            break
  return True


# # TEST CASES
print(anagrams('restful', 'fluster')) # -> True
print(anagrams('cats', 'tocs')) # -> False
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
print(anagrams('paper', 'reapa')) # -> False
print(anagrams('elbow', 'below')) # -> True
print(anagrams('tax', 'taxi')) # -> False
print(anagrams('taxi', 'tax')) # -> False
print(anagrams('night', 'thing')) # -> True
print(anagrams('po', 'popp')) # -> False
print(anagrams('pp', 'oo')) # -> False
