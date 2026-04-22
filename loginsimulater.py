User = {
    "name": "levy",
    "password": "@2001"
}
username = input("enter your name:")
password = input("Enter your password:")

def login(username, password):
    if username == User["name"] and password == User["password"]:
     print ("You have Succesfull")
    else:
     if username != User["name"]: 
      print("Wrong username!!")
     if password != User["password"] :

       print("Wrong password!!")

login(username, password)
