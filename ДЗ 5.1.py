# Ім'я змінної
import string
import keyword
name=input("введить логин:")
invalid_chars = string.punctuation.replace("", "_")
if (name in keyword.kwlist or
    name [0].isdigit() or
    any(c.isupper() for c in name) or
    name.count("_") > 1 or
    any (c in (invalid_chars + " ") for c in name)):
    print (False)
else:
    print (True)


