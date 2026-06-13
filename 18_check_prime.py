#  Check whether the given number is a prime number.
n = int(input("enter a number: "))
if n<=1:
    print("not a prime number")
else:
    is_prime = True
    i=2
    while i<n:
        if n%i==0:
           is_prime = False
           break
        i+=1
    if is_prime:
        print("prime number")
    else:
        print("not prime number") 