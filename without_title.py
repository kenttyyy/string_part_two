# Sample text
text = "hello world"

# Capitalize the first letter of each word without using title()
result = ' '.join(word.capitalize() for word in text.split())

print(result)