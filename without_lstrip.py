# Sample text without lstrip
character = "xxxyHello, World"

# Find the first character that is not x or y using slicing
result = character[character.find('H'):]

print(result)