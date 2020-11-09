print("ax**2 + b*x + c")
a=float(input("input a :"))
b=float(input("input b :"))
c=float(input("input c :"))
print(str(a)+"x",str(b)+"x**2",c)
diskriminant=b**2-4*a*c
root1=(-b-(diskriminant**0.5))/(2*a)
root2=(-b+(diskriminant**0.5))/(2*a)
if diskriminant>0:
    print("there are two real roots")
elif diskriminant==0:
    print("there is one real root")
else:
    print("there are two complex roots")
print("first root :",root1,"second root :",root2)