import random

a = range(1, random.randint(1,30))
print(a)

b = range(1, random.randint(10,40))
print(b)
new_list = []

for num in a:
 if num in b:
  new_list.append(num)

print(new_list)