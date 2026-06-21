a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))
c = int(input("Enter Number 3 : "))
d = int(input("Enter Number 4 : "))

if(a>b and a>c and a>d):
    print("Number 1 is Greatest")
elif(b>a and b>c and b>d):
    print("Number 2 is Greatest")
elif(c>a and c>b and c>d):
    print("Number 3 is Greatest")
else:
    print("Number 4 is Greatest")

print("End")