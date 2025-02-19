s = input("Enter the string: ")  # Read user input
print("The string is:", s)

result = ""
word = ""

# Loop through the string in reverse order
for i in range(len(s) - 1, -1, -1):
    if s[i] == " ":
        result += word + " "  # Add the reversed word and a space
        word = ""  # Reset word storage
    else:
        word = s[i] + word  # Build word in correct order

# Append the last word (which has no space before it)
result += word

print("The reversed string is:", result)
