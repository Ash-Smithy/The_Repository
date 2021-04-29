#include<iostream>
#include<iomanip>
#include<windows.h>
using namespace std;
class A
{
private:
  int x,y;
public:
  A() //empty constructor
  {
    x=20;
    y=50;
  }
  A(int a,int b) //parameterized constructor
  {
    x=a;
    y=b;
  }
  A(A &ob) //copy constructor
  {
    x=ob.x;
    y=ob.y;
  }
  void show() //member function
  {
    cout<<"Value of a is :: "<<x<<"\nValue of B is :: "<<y<<endl;
  }
};

void not_main()
{
  A ob1;
  A ob2(10,70);
  A ob3(ob2);
  cout<<"1st empty constructor"<<endl;
  ob1.show();
  cout<<"\n2nd parameterized constructor"<<endl;
  ob2.show();
  cout<<"\n3rd copy constructor"<<endl;
  ob3.show();
  cout<<"\nThis overall use of constructors is constructor overloading"<<endl;

}
class overload_both
{
private:
  int x,y;
public:
  overload_both(int a,int b)
  {
    x=a;
    y=b;
  }
  overload_both()
  {
    x=0;
    y=0;
  }
  overload_both operator+(overload_both ob)
  {
    overload_both temp;
    temp.x=x+ob.x;
    temp.y=y+ob.y;
    return temp;
  }
  overload_both operator-(overload_both ob)
  {
    overload_both temp;
    temp.x=x-ob.x;
    temp.y=y-ob.y;
    return temp;
  }
  overload_both operator*(overload_both ob)
  {
    overload_both temp;
    temp.x=x*ob.x;
    temp.y=y*ob.y;
    return temp;
  }
  overload_both operator/(overload_both ob)
  {
    overload_both temp;
    temp.x=x/ob.x;
    temp.y=y/ob.y;
    return temp;
  }
  void show()
  {
    cout<<"X = "<<x<<" Y = "<<y<<endl;
  }
  void operator -()
  {
    x=-x;
    y=-y;
  }
};
int not_main2()
{
  overload_both ob1(-10,-20),ob2(15,35),ob3;
  cout<<endl;
  cout<<"members of object 1 :: "<<endl;
  ob1.show();
  -ob1;
  cout<<"After using - operator on ob1 :: "<<endl;
  ob1.show();
  cout<<"The members of object 2 ::"<<endl;
  ob2.show();
  cout<<"\nnow for the binary operators :: "<<endl;
  ob3 = ob1+ob2;
  cout<<"Members of object 1 + object 2 = ";
  ob3.show();
  ob3 = ob1-ob2;
  cout<<"Members of object 1 - object 2 = ";
  ob3.show();
  ob3 = ob1*ob2;
  cout<<"Members of object 1 x object 2 = ";
  ob3.show();
  ob3 = ob1/ob2;
  cout<<"Members of object 1 / object 2 = ";
  ob3.show();
  return 0;
}
int main()
{
  not_main();
  not_main2();
  return 0;
}
