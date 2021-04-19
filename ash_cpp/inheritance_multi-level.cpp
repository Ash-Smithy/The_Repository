#include <iostream>
using namespace std;

class A
{
public:
    int a;
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
public:
    int b;
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
  return obj.display();
}
