# Sample text
text = "HELLO"

# Check if all characters are uppercase without using isupper
result = all('A' <= c <= 'Z' for c in text)

print(result)