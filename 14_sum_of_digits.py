#  Find and print the sum of digits of the given number.
n = int(input("enter number: "))
original_n = n
total = 0
while n>0:
    digit = n%10
    total +=digit
    n = n//10
print(f"The sum of digit of {original_n} is: {total}")