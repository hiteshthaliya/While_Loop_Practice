#Find the HCF (Highest Common Factor) of two given numbers.
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
small = a
if b<a:
    small = b
i = 1
hcf = 1

while i <= small:
    if a%i==0 and b%i==0:
       hcf = i
    i+=1
print("HCF:",hcf)       