gpa=float(input("enter the gpa :"))
num_of_lectures=int(input("enter the number of lectures :"))
if num_of_lectures<47 and gpa<2.0:
  print("Not enough number of lectures and GPA!")

elif num_of_lectures<47 :
   print("Not enough number of lectures!")
elif gpa<2:
  print("Not enough GPA!")
else:
  print("Graduated")