import os
import json

filePath = "./Files/Projects.json"

def fileExistance ():

  if not os.path.exists(filePath):
    with open(filePath, "w") as f:
      json.dump([], f)

def delete (user):
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
    projectID = int(input("\nEnter Project ID to Delete: "))
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
    print("You Are Not Allowed To Delete This Project! ❌")
    return
  
  projects.remove(found)

  with open(filePath, "w") as f:
    json.dump(projects, f, indent=2)

  print("\nProject Deleted Successfully! ✅\n")



