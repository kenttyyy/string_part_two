# Sample text
text = "hello world"

# Capitalize the first letter without using capitalize()
result = (text[0].upper() + text[1:]) if text else text

print(result)