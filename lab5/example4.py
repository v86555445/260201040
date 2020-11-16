password="sdgh456"
while True:
  p=input("Enter password:")
  if p=="help":
    print(password[0])
  elif password!=p:
    print("Wrong")
  else:
    print("Welcome")
    break