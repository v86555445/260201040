age=int(input("enter your age :"))
price=3
if 0<=age<6 or age>60:
  print(price*0, "TL")
elif 6<=age<=18:
  print(price*0.5,"TL")
elif age<0:
  print(" Please write a appropriate age")
else:
  print(price,"TL")