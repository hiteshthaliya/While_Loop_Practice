#Find and print the product of all digits of a given number. 
n = int(input("Enter number: "))
original_n = n
product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n = n // 10    
print(f"Product of digits of {original_n} is: {product}")
