def password_checker(p):
  if len(p)<8 or " " in p:
    return 0
  else:
    level=0
    alpha=False
    numeric=False
    Specialchar=False
    for i in p:
      if i.isnumeric():
        numeric=True
      elif i.isalpha():
        alpha=True
      else:
        Specialchar=True
    if alpha==True:
      level+=1
    if numeric==True:
      level+=1
    if Specialchar==True:
      level+=1
    return level
pw=input("Enter password:")
print("Security level :",password_checker(pw))
