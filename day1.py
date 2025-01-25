# print("hello")
# import keyword
# print(keyword.kwlist)


a=r'\nhi'
print(a)

b='''
iam
rajesh
reddy
'''
print(b)

c="iam" "  student"

print(c)
d="rajesh"

e="reddy"

g=f'hi {d}{e} welcome'

print(g)

print(f'hi {d}{e} welcome')

h="hi"+d+e+'welcome'



i="hello  worlds hello "

print(i[::-1])
print(i[0])


#   https://codeshare.io/cmrbatch1

# 1. What is Python?
# Python is a high-level, interpreted, and dynamically typed programming language known for its simplicity and readability. 
# it contains many in-built libraries and packages. It is both procedure oriented and object oriented programming language.

# 2. Why Python?
#  -Increase Productivity
#  -Easy to learn
#  -Object oriented
#  -Cross Platform
#  -Large Eco system
#  -Becomes a solution for many applications

# 3. Workflow of python?
#  ->Source code converted to Byte code using python compiler
#  ->Byte code converted into Machine code using PVM
#  ->output will be generated
 
# 4. What PVM does?
# 	-PVM: Python Virtual Machine
#   -It is a program which provides programming Environment
#   -PVM converts the byte code instructions into  Machine Code
 
# 5. How to display the output in python?
#   -Use the print() function to display output.

# 6. command to run the Python?
#   -Use python filename.py in the terminal or command prompt

# 7. Datatypes in Python?
#   -Numeric: int, float, complex
#   -Sequence: str, list, tuple,Range
#   -Set: set
#   -Mapping: dict
#   -Boolean: bool
#   -None: NoneType
 
# 8. comments in Python?
#   -Single-line comments: Use #
#   -Multi-line comments: Use triple quotes (''' or """).

# 9. Numeric datatype?
#  -int, float, complex


# 10.What is Identifiers ? Rules for identifiers?
#   -Identifiers are names for variables, functions, etc.
#   Rules:
#   ->Must start with a letter or underscore (_).
#   ->Can include letters, digits, and underscores.
#   ->Cannot be a keyword.
#   ->Case-sensitive.

# 11. Waht are Keywords?
#     Reserved words in Python with predefined meanings

# 12. How to list all keywords?

# import keyword
# print(keyword.kwlist)


# 13. Is Constant available in Python?

# Python doesn’t have built-in constants but uses naming conventions like uppercase (PI = 3.14) to indicate constants.

# 14. If I want to use constant which level i need to implement?
#  -Module level 

# 15. can you give the rules for Constant?
#   -Use uppercase letters with underscores for naming .
#    (e.g., MAX_LENGTH).
#   -Avoid modifying constant values after definition.

# 16. Constant value can be changeable or Not?
#     No we can't change.
#     In python we can change the constant value

# 17. Who will take care of the memory management?

# Python's memory management is handled by the Python interpreter, including garbage collection.

# 18. What are all the way we can define string?
#   -Single quotes: 'hello'
#   -Double quotes: "hello"
#   -Triple quotes: '''hello''' or """hello"""


# 19. specify the ways we can do concatinate the string?
#    -Using +: "hello" + " world"
#    -Using formatted strings: f"hello {name}"
#    -Using join(): " ".join(["hello", "world"])


# 20. What is mean by slicing give an example?
# Extracting parts of a sequence using [start:end:step].
# s = "hello"
# print(s[1:4])
  
# Output: 'ell'

# 21. formatted string?
# A string that embeds variables using {} placeholders or f-strings.
# name = "John"
# print(f"Hello, {name}!")

# 22. sequence types?
#  -str, list, tuple, range.

# 23. can we change value of particular string value using index ?
# No, strings are immutable in Python






