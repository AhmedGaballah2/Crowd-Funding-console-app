import os
import json

filePath = "./Files/Projects.json"

def fileExistance ():

  if not os.path.exists(filePath):
    with open(filePath, "w") as f:
      json.dump([], f)

def view (user):
  fileExistance()
  
  with open(filePath, "r") as f:
    projects = json.load(f)

  myProjects = []

  for project in projects:
    if project["owner_id"] == user["id"]:
      myProjects.append(project)

  if len(myProjects) == 0:
    print("\nNo projects found for you! ❌\n")
    return
  
  print("\n===== My Projects =====\n")

  for project in myProjects:
    print(f"ID: {project['id']}")
    print(f"Title: {project['title']}")
    print(f"Details: {project['details']}")
    print(f"Target: {project['target']}")
    print(f"Start Date: {project['start_date']}")
    print(f"End Date: {project['end_date']}\n")
    print("=" * 30)
    print("")