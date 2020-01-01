#Angstrom number : 153=1^3+5^3+3^3
#Other numbers : 153,370,371,407

x = (input("Enter number = "))
b = len(x)
y=10
x = int(float(x))
for i in range(0,b):
	a = int(float(x%y))
	x=(int(float(abs(x-a))/y))
	p = str(a)
	rems = []
	rems += p
print(rems)