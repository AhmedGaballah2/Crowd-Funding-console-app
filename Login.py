import re
import json
from getpass import getpass
from Operations import Create
from Operations import View
from Operations import Edit
from Operations import Delete
from Operations import Search

emailValidation = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[A-Za-z]{2,}$"
filePath = "./Files/Users.json"

def login ():
  while True:
    email = input("\nEnter your email: ")
    if not re.match(emailValidation, email):
      print("Invalid Input! ❌")
      continue

    password = getpass("Enter your password: ")

    with open(filePath, "r") as f:
      users = json.load(f)
    
    userFound = None

    for user in users:
      if (user["email"] == email):
        userFound = user
        break
    
    if not userFound:
      print(f"Email Doesn't Exist! ❌")
      continue

    if (userFound["password"] == password):
      print(f"Logged In as: {userFound['first_name']} {userFound['last_name']}! ✅\n")
      break
    else:
      print(f"Wrong Password! ❌")
      continue

  while True:
    operation = int(input("1. Create a Project \n2. View All Projects \n3. Edit a Project \n4. Delete a Project \n5. Search for a Project \n6. Back \nChoose an operation: "))

    match operation:
      case 1:
        Create.create(userFound)
      case 2:
        View.view(userFound)
      case 3:
        Edit.edit(userFound)
      case 4:
        Delete.delete(userFound)
      case 5:
        Search.search()
      case 6:
        break
      case _:
        print("Invalid Input! ❌")