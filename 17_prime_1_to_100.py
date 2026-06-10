# Print all prime numbers between 1 and 100. 
# A prime number is a number greater than 1 and
# that has exactly two factors: 1 and itself.
n = 2
while n<=100:
    i=2
    is_prime = True
    while i<n:
        if n%i == 0:
          is_prime =False
          break
        i+=1
    if is_prime:
        print(n)
    n+=1    