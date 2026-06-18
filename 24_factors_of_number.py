#  Print all factors of the given number. 
n = int(input("Enter number: "))
i = 1
print("factors: ",end=" ")        
while i<n:
    if n%i==0:
        print(i,end=" ")
    i+=1