import re

def is_multiline_comment(comment):
    pattern = r'^/\*.*\*/$'
    return re.match(pattern, comment, re.DOTALL) is not None

comment = input("Enter: ")

print(is_multiline_comment(comment))