#Angstrom number : 153=1^3+5^3+3^3
#Other numbers : 153,370,371,407
import math
ang_list = []
number = input("Enter the range : ")
num_initial = 153
p = 1
for the_range in range(0,int(number)):
 x = str(p)
 y = len(x)
 z  = float(x)
 d = z
 a = 0
 for i in range(0,y):
  b = int(d % 10)
  c = b**3
  d = int((d-b)/10)
  a += c
 #print (a)
 # print(d,b)
# a = int(a)
 if a==p :
  ang_list.append(a)
  p+=1
  continue
 else :
  p+=1    
 continue
print(ang_list)
















"""ang_num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,1000)
 for j in range(0,100)
  for k in range(0,10)
   if(i**3+j**3+k**3=i*100+j*10+k*1)
    count += 1
    ang_num[count-1]= i*100+j*10+k*1
    continue
   else:
       continue
print (ang_num)"""
   
 
 
 
 
 
 
 
 
 
 
 
 
 
