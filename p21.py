string=input("Enter your string:")
# # In the first line, print the third character of this string.
print(string[3])

# # In the second line, print the second to last character of this string.
print(string[2],string[-1])

# # In the third line, print the first five characters of this string.
print(string[:5])

# # In the fourth line, print all but the last two characters of this string.
b=len(string)
c=b-2
print(string[:c])

# # In the fifth line, print all the characters of this string with even indices
# # remember indexing starts at 0, so the characters are displayed starting with
# # the first).
print(string[::2])

# # In the sixth line, print all the characters of this string with odd indices 
# # starting with the second character in the string).
print(string[1::2])

# # In the seventh line, print all the characters of the string in reverse order.
print(string[::-1])

# # In the eighth line, print every second character of the string in reverse order,
# # starting from the last one.
print(string[::-2])

# # In the ninth line, print the length of the given string.
print(len(string))