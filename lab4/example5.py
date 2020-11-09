n=int(input("enter a number"))
tot=1
for i in range(n):
  tot=tot*n
  n=n-1
print(tot)