import re

def is_java_identifier(name):
    pattern = r'^[a-zA-Z_$][a-zA-Z\d_$]*$'
    return re.match(pattern, name) is not None


name = input("Enter: ")
print(is_java_identifier(name)) 
