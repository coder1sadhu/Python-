username = input("Enter Username : ")

if(len(username) < 10):
    print("Username Contains less than 10 characters : ",username)
else:
    print("Username Contains more than 10 characters : ",username)