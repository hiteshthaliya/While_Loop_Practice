# Find and print the sum of all factors of the given number
# also Find Largest factor of given number.
n = int(input("Enter number: "))

i = 1
total = 0
largest_factor = 1

print("Factors:", end=" ")

while i < n:
    if n % i == 0:
        print(i, end=" ")
        total += i
        largest_factor = i
    i += 1

print(f"\nSum of factors: {total}")
print(f"Largest factor of given number: {largest_factor}")