import random
def get_rand_list(b,e,N):
  l=[]
  for i in range(N):
    a=random.randint(b,e)
    l.append(a)
  return l
def get_overlap(a,b):
  intersection=set()
  for i in a:
    if i in b:
      intersection.add(i)
  return list(intersection)
a=get_rand_list(0,10,5)
b=get_rand_list(0,10,5)
print(a)
print(b)
print(get_overlap(a,b))
