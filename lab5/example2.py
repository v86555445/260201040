evens=0
n=int(input("How many numbers?"))
t=n
while n>0 :
  num=int(input("Enter an integer :"))
  if num%2==0:
    evens+=1
  n-=1
print((evens*100)/t,"%")