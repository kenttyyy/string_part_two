# Sample text
text = "Hello"

# Center the text within 11 characters without using center()
total_length = 11
spaces = total_length - len(text)
left_spaces = spaces // 2
right_spaces = spaces - left_spaces

result = " " * left_spaces + text + " " * right_spaces

print(result)