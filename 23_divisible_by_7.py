#Print all numbers between a and b that are divisible by 7. 
a = int(input("enter number a : "))
b = int(input("enter number b : "))
i = a
print(f"Number between a and b divisible by 7 are:",end=" ")
while i<b:    
    if i%7 == 0:
            print(i,end=",")
    i+=1                