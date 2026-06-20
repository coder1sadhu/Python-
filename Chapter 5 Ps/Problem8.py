#If the language of two friends are same; what will happen to the program in problem 6?
#it will give the output like no diffference cz names are  not same 
d = {}

name = input("Enter friends name : ")
lan = input("Enter language name : ")

d.update({name:lan})
name = input("Enter friends name : ")
lan = input("Enter language name : ")

d.update({name:lan})
name = input("Enter friends name : ")
lan = input("Enter language name : ")

d.update({name:lan})
name = input("Enter friends name : ")
lan = input("Enter language name : ")

d.update({name:lan})

print(d)