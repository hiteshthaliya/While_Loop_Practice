#Calculate the sum of all even numbers from 1 up to n.
n = int(input("enter number: "))
i = 1
total = 0
while i<=n:
    if i%2==0:
       total += i
    i +=1
print(f"Sum of even number: {total}")     