age=int(input("enter your age :"))
if 0<=age<6 or age>60:
  print("0 TL")
elif 6<=age<=18:
  print("1.5 TL")
elif age<0:
  print(" Please write a appropriate age")
else:
  print("3 TL")