# 1번
def minco(a):
  a=int(a)
  if(0<=a<=10):
    return chr(a+65)
  
  elif(int('A')<=a<=int('Z')):
    return chr(a+1)
k=minco(input())
print(k)