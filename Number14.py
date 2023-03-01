import re

def matches_language(string):
    
    regex = r'^(aa)*(bb|abb|baa|bba|bab)(cc|dd)*$'

   
    return re.match(regex, string) is not None

string = input("Enter the string: ")

print(matches_language(string))
