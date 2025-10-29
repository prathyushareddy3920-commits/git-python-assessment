# Take input from user
string = input("Enter a string: ")

# Convert to lowercase to ignore case sensitivity
string = string.lower()

# Check if the string is equal to its reverse
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")