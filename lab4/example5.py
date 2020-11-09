n=int(input("enter a number"))
tot=1
if n==0:
  print(1)
else:
  for i in range(n):
    tot=tot*n
    n=n-1
  print(tot)