# Sample text
text = "Hello"

# Add spaces at the end to make it 10 characters long without using ljust
result = text + " " * (10 - len(text))

print(result)