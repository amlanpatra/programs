count = 0
ang_num = [0,0,0,0,0,0,0]
for i in range(0,10):
 for j in range(0,10):
  for k in range(0,10):
   if(i**3+j**3+k**3==i*100+j*10+k*1):
    count += 1
    ang_num[count-1]= i*100+j*10+k*1
    continue
   else:
       continue
print (ang_num)