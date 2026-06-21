
#if elif else ladder 

a = int(input("Enter Your Age : ")) 

if(a>=18):
    print("You are eligible for voting")

elif(a<0):
    print("you are entering invalid age")

elif(a==0):
    print("you are entering 0 which is invalid age")

else:
    print("You are not eligible for voting")

print("Program ends!")