#10
#Write code that that lets you know if a string is an integer literal or not.Based on the definition from problem 6
import re

def is_integer(string):
    regex = r'^[-+]?\d+$|^0[0-7]*$|^0[xX][\dA-Fa-f]+'
    return re.match(regex, string) is not None
      
string = input("Enter the value : ")

print("The value is",is_integer(string)) 
