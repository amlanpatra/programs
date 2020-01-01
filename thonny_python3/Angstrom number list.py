
x1 = int((input("Enter the range : ")))
x = 1
x3 = float(x)
a = 0
ang_list = []

for i in range(0,x1):
 y = len(str(float(x)))
 for i in range(0,y):
  b = int(x% 10)
  c = b**3
  d = int((x-b)/10)
  a += int(c)
  #print(x,b)
  # a = int(a)
  if a==x :
   a_str = str(a)
   ang_list.append(a_str)
   x+=1
  else :
   x+=1
 x+=1
print(ang_list)