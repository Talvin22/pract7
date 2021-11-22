def palindrome(s):
    return s == s[::-1]

s = "radar"
i = palindrome(s)
 
if i:
    print("True")
else:
    print("False")