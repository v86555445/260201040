num1=input("Enter number 1:")
num2=input("Enter number 2:")
matching_digits=0
if len(num1)>len(num2):
  for i in range(len(num2)):
    if num1[-i-1]==num2[-i-1]:
      matching_digits+=1
else:
  for i in range(len(num1)):
      if num1[-i-1]==num2[-i-1]:
        matching_digits+=1
print(matching_digits)