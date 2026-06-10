# Check whether the given number is a Perfect number.
'''A Perfect Number is a number that is equal to the
 sum of its factors (excluding the number itself).
 example = 6,28,496,.....'''
n = int(input("enter number: "))
sum = 0
i = 1
while i<n:
     if n%i ==0:
         sum +=i
     i+=1
if sum == n:
    print("perfect number")
else:
    print("Not Perfact number")   