# Count and print the total number of digits in a given number.
n=int(input("enter number: "))
counter = 0

while n>0 :
    n = n // 10 # floor division
    counter += 1

print("total number of digit is: ",counter)        
