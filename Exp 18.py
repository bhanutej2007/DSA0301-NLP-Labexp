import re

expression = input("Enter FOPC expression: ")

pattern = r'^[A-Za-z]+\([A-Za-z]+(,[A-Za-z]+)*\)$'

if re.match(pattern, expression):
    print("Valid FOPC Expression")
else:
    print("Invalid FOPC Expression")