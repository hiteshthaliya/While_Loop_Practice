#  Reverse the given number and print the reversed value.
n = int(input("enter nummber: "))
reverse = 0

if n==0:
    reverse = 0
else:
    while n>0:
       digit = n%10
       reverse = reverse*10 + digit
       n = n//10
       
print(reverse)    