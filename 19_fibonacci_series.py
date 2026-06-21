#  Print the Fibonacci series up to n terms
n = int(input("Enter the number for fibonacci series: "))
a , b = 0 , 1
count = 0
print("Fibonacci series : ",end=" ")
while count<n:
    print(a,end=" ")
    c = a + b
    a = b
    b = c
    count +=1