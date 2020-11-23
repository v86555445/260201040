email=input("enter an e-mail :")
c="ceng113@example.com"
email=email.lower()
email1=email.split("@")
before=email1[0]
after=email1[1]
newbefore=""
for i in before:
  if i!=".":
    newbefore+=i
 
if c==newbefore+"@"+after :
  print("yes")
else:
  print("no")