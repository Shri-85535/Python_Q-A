# In place Swapping of Variables
# Reverse a String in Python
# Creating a Single string from all the elements in the list
# Chaining of Comparision Operator
# Print The File Path Of Imported Modules.
# ENUM Enums (Enumertion) are lists of constants.
# Return Multiple Values From Functions.
# Find the most Frequent Value in A list
# In place Swapping of Variables
# Check the Memory usage of an Object
# Print string N times.
# Check if the two words are 'Anagrams'

x, y  = 10, 20
x, y = y, x
print(x, y) #>>> 20 10
#-------------------------------------------------------------------------

# Reverse a String in Python
list = "Python is Best"
print(list[::-1]) #>>> tseB si nohtyP
#-------------------------------------------------------------------------

# Creating a Single string from all the elements in the list
list = ['A','K','A','S','H']
print("".join(list)) #>>> AKASH
#-------------------------------------------------------------------------

# Chaining of Comparision Operator
n = 10
print(1 < n < 20) #>>> True
print(1 > n <= 20) #>>> False
#-------------------------------------------------------------------------

# Print The File Path Of Imported Modules.
import os
import random
print(os) #>>> <module 'os' from '/usr/lib/python3.6/os.py'>
print(random) #>>> <module 'random' from '/usr/lib/python3.6/random.py'>
#-------------------------------------------------------------------------

# ENUM Enums (Enumertion) are lists of constants. When you need a predefined
#list of values which do represent some kind of numeric or textual data, you
#should use an enum. You should always use enums when a variable (especially
#a method parameter) can only take one out of a small set of possible values.
class BestProgram:
    Python, Is, Python = range(3)

print(BestProgram.Python) #>>> 2
print(BestProgram.Is) #>>> 1
#-------------------------------------------------------------------------

# Return Multiple Values From Functions.
def x():
    return 1, 2, 3, 4

a, b, c, d = x()
print(a, b, c, d) #>>> 1 2 3 4
#-------------------------------------------------------------------------

# Find the most Frequent Value in A list
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key=test.count)) #>>> 4
'''
a = set(test)
b = max(a, key=test.count)
print(b)
'''
#-------------------------------------------------------------------------
 
# Check the Memory usage of an Object
import sys
x = 5
print(sys.getsizeof(x)) #>>> 14 (Answer may differ depends upon system compiler)
#-------------------------------------------------------------------------

# Print string N times.
N = 3
string_to_print = 'Que'
print(string_to_print * N) #>>> QueQueQue
#-------------------------------------------------------------------------

# Check if the two words are 'Anagrams'
#An anagram is a word or phrase formed by rearranging the letters of a
#different word or phrase, typically using all the original
#letters exactly once. (Example : LISTEN x SILENT)
from collections import Counter
def is_Anagram(str1, str2):
    return Counter(str1) == Counter(str2)
print(is_Anagram('slip', 'plis')) #>>> True
print(is_Anagram('cook', 'book')) #>>> True
#-------------------------------------------------------------------------