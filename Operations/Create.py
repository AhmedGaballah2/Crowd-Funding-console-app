import os
import json
from datetime import datetime

filePath = "./Files/Projects.json"


def fileExistance ():

  if not os.path.exists(filePath):
    with open(filePath, "w") as f:
      json.dump([], f)

def create (user):
  fileExistance()
  
  while True:
    title = input("\nEnter your project's title: ")
    if (title == ""):
      print("Title Can't be Empty! ❌")
      continue
    if (len(title) < 10):
      print("Title Must be 10 or More Characters! ❌")
      continue
    if (len(title) > 30):
      print("Title Must be less than 30 Characters! ❌")
      continue
    break

  while True:
    details = input("\nEnter the details of your project: ")
    if (details == ""):
      print("Details Can't be Empty! ❌")
      continue
    if (len(details) < 10):
      print("Details Must be 10 or More Characters! ❌")
      continue
    if (len(details) > 100):
      print("Details Must be less than 100 Characters! ❌")
      continue
    break

  while True:
    target = input("\nEnter your total target: ")
    if (target == ""):
      print("Target Can't be Empty! ❌")
      continue
    elif (not target.isdigit()):
      print("Target Must be a Number! ❌")
      continue
    
    target = int(target)

    if (target <= 0):
      print("Target Must be Greater Than 0! ❌")
      continue
    break
  
  while True:
    startDate = input("\nEnter your start date (YYYY-MM-DD): ")
    try:
      datetime.strptime(startDate, "%Y-%m-%d")
      break
    except:
      print("Invalid Date Format! ❌")
      continue
  
  while True:
    endDate = input("\nEnter your end date (YYYY-MM-DD): ")
    try:
      datetime.strptime(endDate, "%Y-%m-%d")

      start = datetime.strptime(startDate, "%Y-%m-%d")
      end = datetime.strptime(endDate, "%Y-%m-%d")

      if (end <= start):
        print("End date must be after start date! ❌")
        continue
      break
    except:
      print("Invalid Date Format! ❌")
      continue
  
  with open(filePath, "r") as f:
    projects = json.load(f)

  id = len(projects) + 1

  project = {
    "id": id,
    "owner_id": user["id"],
    "title": title,
    "details": details,
    "target": target,
    "start_date": startDate,
    "end_date": endDate
  }

  addProject(project)
  print("Project Created Successfully! ✅")


def addProject(project):
  fileExistance()

  with open(filePath, "r") as f:
    projects = json.load(f)

  projects.append(project)

  with open(filePath, "w") as f:
    json.dump(projects, f, indent=2)

