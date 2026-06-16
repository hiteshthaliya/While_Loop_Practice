#  Find and print the sum of the Fibonacci series up to n terms.
n = int(input("Enter number: "))
a,b = 0,1
count = 0
total = 0

while count <n:
    print(a,end=" ")
    total +=a
    c = a+b
    a = b
    b = c
    count +=1
print(f"\ntotal sum of given fibonacci series: {total}")    