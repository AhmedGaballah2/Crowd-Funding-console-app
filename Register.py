import re
import json
import os
from getpass import getpass

stringValidation = r"^[A-Za-z]+$"
emailValidation = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[A-Za-z]{2,}$"
phoneValidation = r"^01[0125][0-9]{8}$"
filePath = "./Files/Users.json"

def fileExistance ():
  os.makedirs(os.path.dirname(filePath), exist_ok=True)

  if not os.path.exists(filePath):
    with open(filePath, "w") as f:
      json.dump([],f)

def register ():
  fileExistance()

  while True:
    firstName = input("\nEnter your first name: ")
    if re.match(stringValidation, firstName):
      break
    else:
      print("Invalid Input! ❌")

  while True:
    lastName = input("Enter your last name: ")
    if re.match(stringValidation, lastName):
      break
    else:
      print("Invalid Input! ❌")

  while True:
    email = input("Enter your email: ")
    if not re.match(emailValidation, email):
      print("Invalid Input! ❌")
      continue

    with open(filePath, "r") as f:
        users = json.load(f)

    exists = False

    for user in users:
      if (user["email"] == email):
        exists = True
        break

    if exists:
      print("Email Already Exist! ❌")
      continue
    break

  while True:
    password = getpass("Enter your password: ")
    if len(password) < 8:
      print("Password must be at least 8 characters! ❌")
      continue
    
    if not re.search(r"[a-z]", password):
        print("Password must contain a lowercase letter! ❌")
        continue
    
    if not re.search(r"[A-Z]", password):
        print("Password must contain a uppercase letter! ❌")
        continue
    
    if not re.search(r"\d", password):
        print("Password must contain a number! ❌")
        continue
    
    if not re.search(r"[@$!%*?&]", password):
        print("Password must contain a special character! ❌")
        continue
    
    break

  while True:
    confirmPassword = getpass("Re-Enter your password: ")
    if (confirmPassword == password):
      break
    else:
      print("Try Again! ❌")

  while True:
    phone = input("Enter your phone number: ")
    if re.match(phoneValidation, phone):
      break
    else:
      print("Invalid Input! ❌")

  with open(filePath, "r") as f:
    users = json.load(f)

  newID = len(users) + 1

  user = {
    "id": newID, 
    "first_name": firstName,
    "last_name": lastName,
    "email": email,
    "password": password,
    "phone": phone
  }

  addUser(user)
  print("User Registered Successfully! ✅")


def addUser (user):
  fileExistance()

  with open(filePath, "r") as f:
    users = json.load(f)

  users.append(user)

  with open(filePath, "w") as f:
    json.dump(users, f, indent=4)