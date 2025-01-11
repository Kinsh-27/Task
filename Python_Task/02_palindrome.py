# Write a function to check if a given string is a palindrome.

s = input("Enter a string : ")

r = (s[::-1])

if r == s:
    print("string is a palindrome")
else:
    print("string is not a palindrome")