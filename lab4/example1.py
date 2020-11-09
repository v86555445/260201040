num=int(input("enter an integer  :"))
if num <10:
  print(num)
else:
  print(int(str(num%100)[0]) + int(str(num%100)[1]))