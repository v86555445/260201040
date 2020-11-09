a=int(input("enter a "))
b=int(input("enter b "))
c=1
if b>=0:
  for i in range(b):
    c=c*a
  print(c)
else:
  for i in range(-b):
    c=c/a
  print(c)