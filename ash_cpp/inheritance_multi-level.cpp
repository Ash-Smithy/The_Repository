#include <iostream>
using namespace std;

class A
{
  int a;
public:
  void seta()
  {
    a=10;
  }
  int geta()
  {
    return a;
  }
};

class B:public A
{
  int b;
public:
  void setb()
  {
    b=20;
  }
  int getb()
  {
    return b;
  }
};
class C:public B
{
  int c;
public:
  void setc()
  {
    c=geta()*getb();
  }
  void display()
  {
    cout << "C= " << c;
  }
};

int main()
{
  C obj;
  obj.setc();
  obj.display();
  return 0;
}
