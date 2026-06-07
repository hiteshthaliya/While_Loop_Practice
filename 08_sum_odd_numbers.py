# Calculate the sum of all odd numbers from 1 up to n
n = int(input("enter number: "))
i = 0
total = 0
while i<=n:
    if i%2 != 0: # condition for odd 
       total += i
    i += 1
print(f"sum of odd number : {total}")    