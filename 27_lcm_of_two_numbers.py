# Find the LCM (Least Common Multiple) of two given numbers. 
a = int(input("Enter number a:"))
b = int(input("Enter number b:"))
larger = max(a,b)
for i in range(larger,a*b+1):
    if i%a==0 and i%b==0:
        lcm = i
        break
print("LCM:",lcm)    