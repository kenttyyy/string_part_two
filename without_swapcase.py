# Sample text
text = "HeLLo WoRLD"

# Reverse the casing of each character without using swapcase()
result = ""
for c in text:
    if 'a' <= c <= 'z':
        result += chr(ord(c) - 32)
    elif 'A' <= c <= 'Z':
        result += chr(ord(c) + 32)
    else:
        result += c

print(result)