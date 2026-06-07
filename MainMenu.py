import Login
import Register

print("Welcome to 'Crowd-Funding console app'👋")

while True:
  operation = int(input("\n1. Register \n2. Login \n3. Exit \nChoose an operation:"))

  match operation:
    case 1:
      Register.register()
    case 2:
      Login.login()
    case 3:
      break
    case _:
      print("Invalid Input!")