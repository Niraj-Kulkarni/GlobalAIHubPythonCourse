# Creating a login application #

name = "abc@gmail.com"  #creating a predefined username
password_ = "password"   #creating a predefined password

#Taking user input 
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

#Checking the values

if username == name and password == password_:
    print("Login Sucessful.")
else:
    print("Invalid username or password.Please try again.")
