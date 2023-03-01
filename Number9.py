#9
#(15 points) Write code that that lets you know if a string is an floating point literal or not. Based on the definition from problem 4.

import re

def is_float(value):
    
    regex = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
  
    return bool(re.fullmatch(regex, value))

value = input("Enter the value : ")

print("The value is",is_float(value)) 


