#  Check whether the given number is a palindrome.

# A number is a palindrome if it remains the same
#    when its digits are reversed.
n = int(input("enter number: "))
original = n
reverse = 0

while n>0:
    digit = n%10  
    reverse = reverse*10 + digit
    n = n//10  

if reverse == original:
        print("palindrome number")
else:
        print("Not a Palindrom number")