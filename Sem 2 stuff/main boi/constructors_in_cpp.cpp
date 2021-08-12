#include<iostream>
#include<iomanip>
using namespace std;
class A
{
  int a,b;
public:
  A() //no argument constructor or default constructor!!
  {
    a = 10;
    b = 20;
  }
  A(int x,int y)//parameterized constructor
  {
    a =x;
    b=y;
  }
  A(A &ob)//copy constructor
  {
    a=ob.a;
    b = ob.b;
  }
  void show()
  {
    cout<<"A = "<<a<<endl;
    cout<<"B = "<<b<<endl;
  }
};
int main()
{
  A obj;
  A obj1(20,30);
  A obj3=obj;
  obj.show();
  cout<<"Using second constructor :: "<<endl;
  obj1.show();
  cout<<"Using third constructor :: "<<endl;
  obj3.show();
  return 0;
}
