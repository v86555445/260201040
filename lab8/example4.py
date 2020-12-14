def binary_to_dec(n):
  n=str(n)
  num=0
  for i in range(1,len(n)+1):
    if int(n[-i])==1:
      num+=2**(i-1)
  return num
def dec_to_binary(d):
  b = ""
  while d > 0:
    b += str(d%2)
    d //= 2
  return(b[::-1])
print(dec_to_binary(16)) 
print(binary_to_dec(10010))