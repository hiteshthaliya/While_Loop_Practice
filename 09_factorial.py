# Calculate and print the factorial of a given number. 
n = int(input("enter number: "))
i = 1
fact = 1

while i<=n:
    fact *= i
    i +=1
print(f"Factorial of {n} is : {fact}")          
