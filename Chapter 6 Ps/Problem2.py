Phy = int(input("Enter marks of Physics : "))
chem = int(input("Enter marks of Chemistry : "))
maths = int(input("Enter marks of Maths : "))

marks=((Phy+chem+maths)/300)*100

if(marks>=40 and Phy>=33 and chem>=33 and maths>=33):
    print("Congratulation you have scored : " , marks)
else:
    print("Failed marks is : ",marks)