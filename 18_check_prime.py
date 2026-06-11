#  Check whether the given number is a prime number.
n = int(input("enter a number: "))
if n<=1:
    print("not prime")
else:
    is_prime = True
    i=2
    while i<n:
        is_prime = True
        if n%i==0:
           is_prime = False
           break
        i+=1
    if is_prime:
        print("prime number")
    else:
        print("not prime number")   