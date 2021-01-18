a_list=[22,8,12,-4,27,30,36,50,7,68,91,56,2,85,42,98,25]
while True:
  n=0
  for i in range(len(a_list)):
    min=a_list[i]
    min_index=i
    for j in range(i+1,len(a_list)):
      print(i)
      if a_list[j]<min:
        min=a_list[j]
        min_index=j
    a_list[n],a_list[min_index]=a_list[min_index],a_list[n]
    n+=1
    if n==len(a_list):
      break
    print(a_list)
  break
print(a_list)