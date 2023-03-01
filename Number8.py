#8
#Write code that that lets you know if a string is an email address or not.Based on the definition from problem 1.


import re

def is_email(email):
   
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
  
    if re.match(regex, email):
        return True
    else:
        return False




email = input("Enter the value : ")

print(is_email(email))  