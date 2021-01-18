def binary_search(a_list,x):
  if len(a_list)==0:
    return -1
  mid_index=(len(a_list)-1)//2
  print(a_list[mid_index])
  if a_list[mid_index]<x:
    print("mid index",mid_index)
    return mid_index+binary_search(a_list[mid_index+1::],x)
  elif a_list[mid_index]>x:
    print("mid index",mid_index)
    return mid_index +binary_search(a_list[:mid_index:],x)
  else:
    print("mid index",mid_index)
    return mid_index
a_list=[22,8,12,-4,27,30,36,50,7,68,91,56,2,85,42,98,25]
a_list.sort()
print(a_list)
print(binary_search(a_list,12))