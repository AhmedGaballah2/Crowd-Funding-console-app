import os
import json
from datetime import datetime

filePath = "./Files/Projects.json"

def fileExistance ():

  if not os.path.exists(filePath):
    with open(filePath, "w") as f:
      json.dump([], f)

def edit (user):
  fileExistance()

  with open(filePath, "r") as f:
    projects = json.load(f)

  if len(projects) == 0:
    print("\nNo Projects Available! ❌\n")
    return
  
  print("\n===== Your Projects =====\n")

  for project in projects:
    if project["owner_id"] == user["id"]:
      print(f"ID: {project['id']} | Title: {project['title']}")

  try:
    projectID = int(input("\nEnter Project ID to Edit: "))
  except:
    print("Invalid ID! ❌")
    return
  
  found = None

  for project in projects:
    if project["id"] == projectID:
      found = project
      break

  if not found:
    print("Project Not Found! ❌")
    return
  
  if found["owner_id"] != user["id"]:
    print("You Are Not Allowed To Edit This Project! ❌")
    return
  
  print("\nWhat do you want to edit?")
  
  while True:
    try:
      operation = int(input("1. Title \n2. Details \n3. Total Target \n4. Start Date \n5. End Date \n6. Back \nChoose an operation: "))
    except:
      print("Invalid Input! ❌")
      continue

    match operation:
      case 1:
        while True:
          newTitle = input("Enter your new project's title: ")
          if (newTitle == ""):
            print("Title Can't be Empty! ❌")
            continue
          if (len(newTitle) < 10):
            print("Title Must be 10 or More Characters! ❌")
            continue
          if (len(newTitle) > 30):
            print("Title Must be less than 30 Characters! ❌")
            continue
          found["title"] = newTitle
          break
      case 2:
        while True:
          newDetails = input("Enter the new details of your project: ")
          if (newDetails == ""):
            print("Details Can't be Empty! ❌")
            continue
          if (len(newDetails) < 10):
            print("Details Must be 10 or More Characters! ❌")
            continue
          if (len(newDetails) > 100):
            print("Details Must be less than 100 Characters! ❌")
            continue
          found["details"] = newDetails
          break
      case 3:
        while True:
          newTarget = input("Enter your new total target: ")
          if (newTarget == ""):
            print("Target Can't be Empty! ❌")
            continue
          elif (not newTarget.isdigit()):
            print("Target Must be a Number! ❌")
            continue
          
          newTarget = int(newTarget)

          if (newTarget <= 0):
            print("Target Must be Greater Than 0! ❌")
            continue
          found["target"] = newTarget
          break
      case 4:
        while True:
          newStart = input("Enter new start date (YYYY-MM-DD): ")
          try:
            datetime.strptime(newStart, "%Y-%m-%d")
            found["start_date"] = newStart
            break
          except:
            print("Invalid Date Format! ❌")
            continue
      case 5:
        while True:
          newEnd = input("Enter new end date (YYYY-MM-DD): ")
          try:
            datetime.strptime(newEnd, "%Y-%m-%d")

            start = datetime.strptime(found["start_date"], "%Y-%m-%d")
            end = datetime.strptime(newEnd, "%Y-%m-%d")

            if (end <= start):
              print("End date must be after start date! ❌")
              continue
            found["end_date"] = newEnd
            break
          except:
            print("Invalid Date Format! ❌")
            continue
      case 6:
        break
      case _:
        print("Invalid Input! ❌")

  with open(filePath, "w") as f:
    json.dump(projects, f, indent=2)
  
  print("Project Updated Successfully! ✅")