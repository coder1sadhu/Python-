#If the names of 2 friends are same; what will happen to the program in problem 6?
#it will give the updated names that is updated last 
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