# Print the square of each number from 1 to n.

# using for loop
n = int(input("Enter number: "))
for i in range(1,n+1):
    square = i**2
    print(square,end=" ")

print()
# using while loop
n = int(input("Enter number: "))
i = 1
while i<=n:
    print(i**2,end=" ")
    i+=1