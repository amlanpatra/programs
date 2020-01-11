# Password generator

import random

a = random.choice('!@#$%^&*()_+}{[]|:;?/>.<,')
b = random.choice('!@#$%^&*()_+}{[]|:;?/>.<,')
p = random.choice('!@#$%^&*()_+}{[]|:;?/>.<,')

c=random.choice('abcdefghijklmnopqrstuvwxyz')
d=random.choice('abcdefghijklmnopqrstuvwxyz')

e=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
f=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

g=str(random.randint(0,9))
h=str(random.randint(0,9))
i=str(random.randint(0,9))
q=str(random.randint(0,9))

j = [a,b,c,d,e,f,g,h,i,p,q]
random.shuffle(j)
print(''.join(j))