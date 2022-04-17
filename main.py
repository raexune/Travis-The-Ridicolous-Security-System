known_users = ["Peter", "Laura", "Ramona", "Elisabeth"]

while True:
  print("Hi, my name is Travis.")
  name = input("What is your name? ").strip().capitalize()
  
  if name in known_users:
    print(f"Hello {name}!")
    remove = input("Would you like to be removed from the list (y/n)?: ").strip().lower()
    if remove == "y":
      known_users.remove(name)
    elif remove == "n":
      print("No problem, i didn`t want you do leave anyway.")
    
  else:
    print(f"Hmmm, i don´t think i have met you yet {name}.")
    add = input("Would you like to be added to the list (y/n)? ").strip().lower()
    if add == "y":
      known_users.append(name)
    elif add == "n":
      print("No worries, see you around!")
