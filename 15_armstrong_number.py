#  Check whether the given number is an Armstrong number. 
'''An Armstrong number is a number that is equal to the sum
  of its digits, where each digit is raised to the power of
  the total number of digits.
  example : 153 = 1^3 + 5^3 + 3^3 = 153'''

num = int(input("enter number: "))
original_n = num
n = len(str(num)) 
total = 0

while num>0:
    digit = num %10
    total  += digit**n
    num = num //10

if total == original_n :
    print("Armstrong number")   
else:
    print("Not a Armstrpng number")