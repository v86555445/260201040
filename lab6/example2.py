num_of_students=int(input("how many students are there ?"))
s=0
al=[]
average_grades=[]
while num_of_students>s:
  md1=float(input("input midterm 1 :"))
  md2=float(input("input midterm 2 :"))
  fnl=float(input("input final :"))
  al.append([md1,md2,fnl])
  average=md1*30/100+md2*30/100+fnl*40/100
  average_grades.append(average)
  s+=1
print("student's grades :",al)
print("average student's grades",average_grades)