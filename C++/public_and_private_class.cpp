#include<iostream.h>
#include<conio.h>
class A
{
private:
int a;
public:
int b;

public:

void show()
{
a=10 ;
b=20;
clrscr();
//Every members can be access here, same class
cout<<"\nAccessing variable within the class"<<endl;

cout<<"Value of a: "<<a<<endl;
cout<<"Value of b: "<<b<<endl;
}
};

void main()
{
A obj; // create object
obj.show();

cout<<"\nAccessing variable outside the class"<<endl;
//'a' cannot be accessed as it is private
//cout<<"value of a: "<<obj.a<<endl;

//'b' is public as can be accessed from any where
cout<<"value of b: "<<obj.b<<endl;

getch();
}